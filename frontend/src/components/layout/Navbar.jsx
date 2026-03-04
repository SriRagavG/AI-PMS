import {
  AppBar,
  Toolbar,
  Typography,
  Button,
  Box,
  IconButton,
  Tooltip
} from "@mui/material";
import { useContext } from "react";
import { AuthContext } from "../../context/AuthContext";
import BrightnessHighIcon from "@mui/icons-material/BrightnessHigh";  // Light mode icon
import BrightnessLowIcon from "@mui/icons-material/BrightnessLow";
import { useTheme } from "../../context/ThemeContext";

const Navbar = () => {
  const { logout } = useContext(AuthContext);
  const { mode, toggleMode } = useTheme();

  return (
    <AppBar position="fixed" sx={{ zIndex: 1201 }}>
      <Toolbar>
        <Typography variant="h6" sx={{ flexGrow: 1 }}>
          AI Procurement Management
        </Typography>

        <Box sx={{ display: "flex", alignItems: "center", gap: 1 }}>
          {/* New: Dark Mode Toggle */}
          <Tooltip title={`Switch to ${mode === "light" ? "dark" : "light"} mode`}>
            <IconButton onClick={toggleMode} color="inherit" size="small">
              {mode === "light" ? <BrightnessLowIcon /> : <BrightnessHighIcon />}
            </IconButton>
          </Tooltip>
          <Button color="inherit" onClick={logout}>
            Logout
          </Button>
        </Box>
      </Toolbar>
    </AppBar>
  );
};

export default Navbar;
