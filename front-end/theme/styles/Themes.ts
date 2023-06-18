import { Dimensions } from "react-native";
// export const ThemeContext = createContext<ThemeProps>

export enum backgroundColors {}
// GMAIL_DARK = 0,
// GMAIL_LIGHT = 1,

export const themes = {
  gmail_dark: "#9F2D2D",
  gmail_light: "#C55A5A",
  discord_dark: "#4D53E8",
  discord_light: "#6B83FD",
  slack_dark: "#832FEE",
  slack_light: "#B678E8 ",
  whatsapp_dark: "#004B30",
  whatsapp_light: "#007320",
};

export const GUTTER = 10;

export const rgb2hsv = (r: number, g: number, b: number) => {
  let v = Math.max(r, g, b),
    c = v - Math.min(r, g, b);
  let h =
    c && (v == r ? (g - b) / c : v == g ? 2 + (b - r) / c : 4 + (r - g) / c);
  return [60 * (h < 0 ? h + 6 : h), v && c / v, v];
};

export const appColor = (app_name: string) => {
  switch (app_name) {
    case "gmail":
      return [themes.gmail_light, themes.gmail_dark];
    case "discord":
      return [themes.discord_light, themes.discord_dark];
    case "slack":
      return [themes.slack_light, themes.slack_dark];
    case "whatsapp":
      return [themes.whatsapp_light, themes.whatsapp_dark];
  }
};

//   export const SCREN_WIDTH
