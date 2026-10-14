import { createFileRoute } from "@tanstack/react-router";
import { useCallback, useEffect, useState } from "react";
import {
  calcularEdad,
  crearAlumno,
  DEFAULT_API_URL,
  fetchAlumnoPorLegajo,
  fetchAlumnos,
  formatearFecha,
  getApiBaseUrl,
  setApiBaseUrl,
  validarAlumno,
  type Alumno,
} from "@/lib/alumnos";

export const Route = createFileRoute("/")({
  head: () => ({
    meta: [
      { title: "Registro de Alumnos — Cliente API" },
      {
        name: "description",
        content:
          "Cliente web para la API de alumnos: listado, búsqueda por legajo y carga de nuevos registros.",
      },
      { property: "og:title", content: "Registro de Alumnos — Cliente API" },
      {
        property: "og:description",
        content:
          "Cliente web para la API de alumnos: listado, búsqueda por legajo y carga de nuevos registros.",
      },
      { property: "og:type", content: "website" },
      { name: "twitter:card", content: "summary" },
    ],
  }),
  component: Index,
});

type EstadoConexion = "conectando" | "conectado" | "error";

function Index() {
  const [urlDraft, setUrlDraft] = useState(getApiBaseUrl());
  const [baseUrl, setBaseUrl] = useState(getApiBaseUrl());
  const [alumnos, setAlumnos] = useState<Alumno[]>([]);
  const [estado, setEstado] = useState<EstadoConexion>("conectando");
  const [errorLista, setErrorLista] = useState<string | null>(null);
  const [ultimaCarga, setUltimaCarga] = useState<number | null>(null);

  const [busqueda, setBusqueda] = useState("");
  const [resultadoBusqueda, setResultadoBusqueda] = useState<Alumno | null>(null);
  const [errorBusqueda, setErrorBusqueda] = useState<string | null>(null);

  const [legajo, setLegajo] = useState("");
  const [nombre, setNombre] = useState("");
  const [apellido, setApellido] = useState("");
  const [fecha, setFecha] = useState("");
  const [errorForm, setErrorForm] = useState<string | null>(null);
  const [exitoForm, setExitoForm] = useState<string | null>(null);
  const [enviando, setEnviando] = useState(false);

  const cargar = useCallback(async () => {
    setEstado("conectando");
    setErrorLista(null);
    const inicio = performance.now();
    try {
      const datos = await fetchAlumnos();
      setAlumnos(datos);
      setEstado("conectado");
      setUltimaCarga(Math.round(performance.now() - inicio));
    } catch (e) {
      setEstado("error");
      setErrorLista(
        e instanceof TypeError
          ? "No se pudo conectar con la API. Verificá la URL, que el túnel esté activo y que CORS esté habilitado en Flask."
          : (e as Error).message,
      );
    }
  }, []);

  useEffect(() => {
    cargar();
  }, [cargar, baseUrl]);

  function guardarUrl(e: React.FormEvent) {
    e.preventDefault();
    if (!urlDraft.trim()) return;
    setApiBaseUrl(urlDraft);
    setBaseUrl(getApiBaseUrl());
  }

  async function buscar(e: React.FormEvent) {
    e.preventDefault();
    setErrorBusqueda(null);
    setResultadoBusqueda(null);
    const n = Number(busqueda);
    if (!busqueda.trim()) return;
    if (!Number.isInteger(n) || n <= 0) {
      setErrorBusqueda("Ingresá un legajo numérico válido.");
      return;
    }
    try {
      setResultadoBusqueda(await fetchAlumnoPorLegajo(n));
    } catch (err) {
      setErrorBusqueda((err as Error).message);
    }
  }

  async function agregar(e: React.FormEvent) {
    e.preventDefault();
    setErrorForm(null);
    setExitoForm(null);
    const alumno: Alumno = {
      legajo: Number(legajo),
      nombre: nombre.trim(),
      apellido: apellido.trim(),
      fechaDeNacimiento: fecha,
    };
    const invalido = validarAlumno(alumno);
    if (invalido) {
      setErrorForm(invalido);
      return;
    }
    setEnviando(true);
    try {
      await crearAlumno(alumno);
      setExitoForm(`${alumno.nombre} ${alumno.apellido} agregado correctamente.`);
      setLegajo("");
      setNombre("");
      setApellido("");
      setFecha("");
      await cargar();
    } catch (err) {
      setErrorForm((err as Error).message);
    } finally {
      setEnviando(false);
    }
  }

  const etiquetaEstado =
    estado === "conectado"
      ? "API conectada"
      : estado === "conectando"
        ? "Conectando…"
        : "Sin conexión";

  return (
    <div className="min-h-screen bg-background text-foreground">
      <header className="sticky top-0 z-20 border-b border-border bg-card backdrop-blur-xl">
        <div className="mx-auto flex max-w-6xl flex-wrap items-center gap-x-6 gap-y-3 px-8 py-4">
          <div className="animate-clip font-display text-2xl font-bold tracking-tight">
            Registro<span className="text-primary">.</span>
          </div>
          <div className="flex items-center gap-2 rounded-full bg-card px-3 py-1.5 outline-1 outline-border">
            <span
              className={`h-1.5 w-1.5 rounded-full ${
                estado === "conectado"
                  ? "bg-primary"
                  : estado === "conectando"
                    ? "bg-muted-foreground"
                    : "bg-destructive"
              }`}
            />
            <span className="font-mono text-[11px] uppercase tracking-[0.14em] text-muted-foreground">
              {etiquetaEstado}
            </span>
          </div>
          <form onSubmit={guardarUrl} className="flex min-w-0 flex-1 items-center gap-2">
            <label className="flex min-w-0 flex-1 items-center gap-2 rounded-xl bg-card px-3 py-2 outline-1 outline-border">
              <span className="font-mono text-[11px] uppercase tracking-[0.14em] text-muted-foreground">
                URL
              </span>
              <input
                className="min-w-0 flex-1 bg-transparent font-mono text-sm text-foreground outline-none"
                value={urlDraft}
                onChange={(e) => setUrlDraft(e.target.value)}
                placeholder={DEFAULT_API_URL}
                aria-label="URL base de la API"
              />
            </label>
            <button
              type="submit"
              className="rounded-xl bg-primary px-4 py-2 text-sm font-medium text-primary-foreground transition-[background,transform] duration-200 hover:-translate-y-0.5 hover:bg-primary/90"
            >
              Guardar
            </button>
          </form>
        </div>
      </header>

      <main className="mx-auto grid max-w-6xl gap-10 px-8 py-10 lg:grid-cols-[minmax(0,1fr)_360px]">
        <section>
          <div className="mb-6 flex flex-wrap items-end justify-between gap-3">
            <h1 className="font-display text-4xl font-semibold tracking-tight text-balance">
              Alumnos
            </h1>
            <form
              onSubmit={buscar}
              className="flex items-center gap-2 rounded-xl bg-card px-3 py-2 outline-1 outline-border"
            >
              <span className="font-mono text-[11px] uppercase tracking-[0.14em] text-muted-foreground">
                Buscar legajo
              </span>
              <input
                className="w-24 bg-transparent font-mono text-sm outline-none"
                placeholder="20240001"
                aria-label="Buscar por legajo"
                value={busqueda}
                onChange={(e) => setBusqueda(e.target.value)}
              />
            </form>
          </div>

          {(resultadoBusqueda || errorBusqueda) && (
            <div className="animate-rise mb-4 rounded-2xl bg-card px-5 py-3 outline-1 outline-border backdrop-blur-xl">
              {resultadoBusqueda ? (
                <span className="text-sm">
                  <span className="font-mono text-xs text-muted-foreground">
                    {resultadoBusqueda.legajo}
                  </span>{" "}
                  <span className="font-medium">
                    {resultadoBusqueda.nombre} {resultadoBusqueda.apellido}
                  </span>{" "}
                  <span className="font-mono text-xs text-muted-foreground">
                    · {formatearFecha(resultadoBusqueda.fechaDeNacimiento)}
                  </span>
                </span>
              ) : (
                <span className="text-sm text-destructive">{errorBusqueda}</span>
              )}
            </div>
          )}

          <div className="rounded-2xl bg-card outline-1 outline-border backdrop-blur-xl">
            <div className="grid grid-cols-[88px_1fr_1fr_120px_64px] gap-4 border-b border-border px-5 py-3 font-mono text-[11px] uppercase tracking-[0.14em] text-muted-foreground">
              <span>Legajo</span>
              <span>Nombre</span>
              <span>Apellido</span>
              <span>Nacimiento</span>
              <span className="text-right">Edad</span>
            </div>

            {estado === "conectando" && (
              <p className="px-5 py-6 text-sm text-muted-foreground">Cargando alumnos…</p>
            )}

            {estado === "error" && (
              <div className="px-5 py-6">
                <p className="text-sm text-destructive">{errorLista}</p>
                <button
                  onClick={cargar}
                  className="mt-3 rounded-xl bg-primary px-4 py-2 text-sm font-medium text-primary-foreground transition-[background,transform] duration-200 hover:-translate-y-0.5 hover:bg-primary/90"
                >
                  Reintentar
                </button>
              </div>
            )}

            {estado === "conectado" && alumnos.length === 0 && (
              <p className="px-5 py-6 text-sm text-muted-foreground">
                No hay alumnos cargados todavía.
              </p>
            )}

            {estado === "conectado" &&
              alumnos.map((a, i) => (
                <div
                  key={a.legajo}
                  className="animate-rise"
                  style={{ animationDelay: `${i * 60}ms` }}
                >
                  <div className="grid grid-cols-[88px_1fr_1fr_120px_64px] items-center gap-4 border-b border-border px-5 py-3 text-sm transition-colors duration-200 last:border-b-0 hover:bg-background/60">
                    <span className="font-mono text-xs text-muted-foreground">{a.legajo}</span>
                    <span className="font-medium">{a.nombre}</span>
                    <span className="font-medium">{a.apellido}</span>
                    <span className="font-mono text-xs">
                      {formatearFecha(a.fechaDeNacimiento)}
                    </span>
                    <span className="text-right font-mono text-xs">
                      {calcularEdad(a.fechaDeNacimiento)}
                    </span>
                  </div>
                  <div
                    className="animate-bar h-px bg-primary/45"
                    style={{ animationDelay: `${120 + i * 60}ms` }}
                  />
                </div>
              ))}
          </div>

          <div className="mt-4 flex items-center gap-2 rounded-2xl bg-card px-4 py-2.5 outline-1 outline-border backdrop-blur-xl">
            <span className="font-mono text-[11px] text-muted-foreground">GET /alumnos</span>
            <span className="font-mono text-[11px] text-muted-foreground">·</span>
            <span className="font-mono text-[11px] text-muted-foreground">
              {estado === "conectado"
                ? `${alumnos.length} registros · 200 OK · ${ultimaCarga ?? 0} ms`
                : estado === "conectando"
                  ? "Cargando…"
                  : "Error de conexión"}
            </span>
          </div>
        </section>

        <aside
          className="animate-rise rounded-2xl bg-card p-6 outline-1 outline-border backdrop-blur-xl"
          style={{ animationDelay: "220ms" }}
        >
          <h2 className="font-display text-xl font-semibold tracking-tight text-balance">
            Nuevo alumno
          </h2>
          <p className="mt-1 text-sm text-pretty text-muted-foreground">
            POST /alumnos · los campos se validan al enviar.
          </p>
          <form onSubmit={agregar} className="mt-5 space-y-4">
            <label className="block">
              <span className="font-mono text-[11px] uppercase tracking-[0.14em] text-muted-foreground">
                Legajo
              </span>
              <input
                className="mt-1 w-full rounded-xl bg-background px-3 py-2 text-sm outline-1 outline-border focus:outline-ring"
                value={legajo}
                onChange={(e) => setLegajo(e.target.value)}
                placeholder="20240005"
                inputMode="numeric"
              />
            </label>
            <label className="block">
              <span className="font-mono text-[11px] uppercase tracking-[0.14em] text-muted-foreground">
                Nombre
              </span>
              <input
                className="mt-1 w-full rounded-xl bg-background px-3 py-2 text-sm outline-1 outline-border focus:outline-ring"
                value={nombre}
                onChange={(e) => setNombre(e.target.value)}
                placeholder="Lucía"
              />
            </label>
            <label className="block">
              <span className="font-mono text-[11px] uppercase tracking-[0.14em] text-muted-foreground">
                Apellido
              </span>
              <input
                className="mt-1 w-full rounded-xl bg-background px-3 py-2 text-sm outline-1 outline-border focus:outline-ring"
                value={apellido}
                onChange={(e) => setApellido(e.target.value)}
                placeholder="Arrieta"
              />
            </label>
            <label className="block">
              <span className="font-mono text-[11px] uppercase tracking-[0.14em] text-muted-foreground">
                Nacimiento
              </span>
              <input
                type="date"
                className="mt-1 w-full rounded-xl bg-background px-3 py-2 text-sm outline-1 outline-border focus:outline-ring"
                value={fecha}
                onChange={(e) => setFecha(e.target.value)}
                max={new Date().toISOString().slice(0, 10)}
              />
            </label>
            <button
              type="submit"
              disabled={enviando}
              className="w-full rounded-xl bg-primary px-4 py-2.5 text-sm font-medium text-primary-foreground transition-[background,transform] duration-200 hover:-translate-y-0.5 hover:bg-primary/90 disabled:opacity-60"
            >
              {enviando ? "Agregando…" : "Agregar alumno"}
            </button>
            {errorForm && <p className="text-sm text-destructive">{errorForm}</p>}
            {exitoForm && <p className="text-sm text-primary">{exitoForm}</p>}
          </form>
          <p className="mt-4 text-[11px] leading-relaxed text-muted-foreground">
            Requisitos: legajo numérico mayor a 0, nombre y apellido con mayúscula inicial y
            sin números, fecha de nacimiento no futura.
          </p>
        </aside>
      </main>
    </div>
  );
}
