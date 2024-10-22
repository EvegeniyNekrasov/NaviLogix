export function isAuthenticated() {
    return localStorage.getItem("auth") === "true";
}

export async function logIn() {
    localStorage.setItem("auth", "true");
}

export async function logOut() {
    localStorage.removeItem("auth");
}
