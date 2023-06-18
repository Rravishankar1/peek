// export const ThemeContext = createContext<ThemeProps>

export enum backgroundColors {
    // GMAIL_DARK = 0,
    // GMAIL_LIGHT = 1,
}

export const themes = {
    "gmail_dark": "#504040",
    "gmail_light": "#9E0A0A"
}

export const GUTTER = 10;

export const rgb2hsv = (r: number, g: number, b: number) => {
    let v=Math.max(r,g,b), c=v-Math.min(r,g,b);
    let h= c && ((v==r) ? (g-b)/c : ((v==g) ? 2+(b-r)/c : 4+(r-g)/c)); 
    return [60*(h<0?h+6:h), v&&c/v, v];
  }