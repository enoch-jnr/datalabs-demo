import { createContext, useContext, useEffect, useState, ReactNode } from "react";
import { fetchMe, loginUser, registerUser } from "@/api/auth";
import { User } from "@/api/types";

interface AuthContextValue {
  user: User | null;
  isLoading: boolean;
  login: (email: string, password: string) => Promise<void>;
  signup: (payload: {
    email: string;
    password: string;
    first_name: string;
    last_name: string;
  }) => Promise<void>;
  logout: () => void;
}

const AuthContext = createContext<AuthContextValue | undefined>(undefined);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const token = localStorage.getItem("dl_access_token");
    if (!token) {
      setIsLoading(false);
      return;
    }
    fetchMe()
      .then(setUser)
      .catch(() => {
        localStorage.removeItem("dl_access_token");
        localStorage.removeItem("dl_refresh_token");
      })
      .finally(() => setIsLoading(false));
  }, []);

  async function login(email: string, password: string) {
    const tokens = await loginUser(email, password);
    localStorage.setItem("dl_access_token", tokens.access_token);
    localStorage.setItem("dl_refresh_token", tokens.refresh_token);
    setUser(await fetchMe());
  }

  async function signup(payload: {
    email: string;
    password: string;
    first_name: string;
    last_name: string;
  }) {
    await registerUser(payload);
    await login(payload.email, payload.password);
  }

  function logout() {
    localStorage.removeItem("dl_access_token");
    localStorage.removeItem("dl_refresh_token");
    setUser(null);
  }

  return (
    <AuthContext.Provider value={{ user, isLoading, login, signup, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth(): AuthContextValue {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("useAuth must be used within AuthProvider");
  return ctx;
}
