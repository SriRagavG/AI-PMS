// src/context/ThemeContext.jsx (Fixed import for CssBaseline)
import { createContext, useContext, useState, useEffect } from "react";
import { ThemeProvider, createTheme } from "@mui/material/styles";  // createTheme & ThemeProvider from styles
import { CssBaseline } from "@mui/material";  // Fixed: CssBaseline from material

const ThemeContext = createContext();

export const useTheme = () => useContext(ThemeContext);

export const ThemeProviderWrapper = ({ children }) => {
  const [mode, setMode] = useState("light");

  useEffect(() => {
    const savedMode = localStorage.getItem("themeMode") || "light";
    setMode(savedMode);
    document.documentElement.setAttribute("data-theme", savedMode);
  }, []);

  const toggleMode = () => {
    const newMode = mode === "light" ? "dark" : "light";
    setMode(newMode);
    localStorage.setItem("themeMode", newMode);
    document.documentElement.setAttribute("data-theme", newMode);
  };

  const theme = createTheme({
    palette: {
      mode,
    },
  });

  return (
    <ThemeContext.Provider value={{ mode, toggleMode }}>
      <ThemeProvider theme={theme}>
        <CssBaseline />  {/* Applies theme globally */}
        {children}
      </ThemeProvider>
    </ThemeContext.Provider>
  );
};