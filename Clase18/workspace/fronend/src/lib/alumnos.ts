export interface Alumno {
  legajo: number;
  nombre: string;
  apellido: string;
  fechaDeNacimiento: string; // ISO yyyy-mm-dd
}

const STORAGE_KEY = "alumnos-api-base-url";
export const DEFAULT_API_URL = "https://lg3zkhvf-5000.brs.devtunnels.ms";

export function getApiBaseUrl(): string {
  if (typeof window === "undefined") return DEFAULT_API_URL;
  return window.localStorage.getItem(STORAGE_KEY) || DEFAULT_API_URL;
}

export function setApiBaseUrl(url: string): void {
  window.localStorage.setItem(STORAGE_KEY, url.trim().replace(/\/+$/, ""));
}

async function parseError(res: Response): Promise<never> {
  let detail = `Error ${res.status}`;
  try {
    const body = await res.json();
    if (body?.error) detail = body.error;
  } catch {
    // respuesta sin JSON
  }
  throw new Error(detail);
}

export async function fetchAlumnos(): Promise<Alumno[]> {
  const res = await fetch(`${getApiBaseUrl()}/alumnos`);
  if (!res.ok) await parseError(res);
  return res.json();
}

export async function fetchAlumnoPorLegajo(legajo: number): Promise<Alumno> {
  const res = await fetch(`${getApiBaseUrl()}/alumnos/${legajo}`);
  if (!res.ok) await parseError(res);
  return res.json();
}

export async function crearAlumno(alumno: Alumno): Promise<Alumno> {
  const res = await fetch(`${getApiBaseUrl()}/alumnos`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(alumno),
  });
  if (!res.ok) await parseError(res);
  return res.json();
}

export function calcularEdad(fechaIso: string): number {
  const nacimiento = new Date(`${fechaIso}T00:00:00`);
  const hoy = new Date();
  let edad = hoy.getFullYear() - nacimiento.getFullYear();
  const m = hoy.getMonth() - nacimiento.getMonth();
  if (m < 0 || (m === 0 && hoy.getDate() < nacimiento.getDate())) edad--;
  return edad;
}

export function formatearFecha(fechaIso: string): string {
  const [y, m, d] = fechaIso.split("-");
  return `${d}/${m}/${y}`;
}

/** Mismas reglas que el modelo Alumno del backend. */
export function validarAlumno(a: Alumno): string | null {
  if (!Number.isInteger(a.legajo) || a.legajo <= 0)
    return "El legajo debe ser un número mayor que 0.";
  const nombreOk = /^[A-ZÁÉÍÓÚÑ][a-záéíóúñA-ZÁÉÍÓÚÑ]*$/;
  if (!a.nombre) return "El nombre no puede estar vacío.";
  if (!nombreOk.test(a.nombre))
    return "El nombre debe comenzar con mayúscula y no contener espacios ni números.";
  if (!a.apellido) return "El apellido no puede estar vacío.";
  if (!nombreOk.test(a.apellido))
    return "El apellido debe comenzar con mayúscula y no contener espacios ni números.";
  if (!a.fechaDeNacimiento) return "La fecha de nacimiento es obligatoria.";
  if (new Date(`${a.fechaDeNacimiento}T00:00:00`) > new Date())
    return "La fecha de nacimiento no puede ser futura.";
  return null;
}
