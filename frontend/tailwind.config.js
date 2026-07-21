/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        "dl-blue": "#4285F4",
        "dl-green": "#34A853",
        "dl-yellow": "#FBBC05",
        "dl-red": "#EA4335",
      },
      fontFamily: {
        sans: ["Inter", "Roboto", "system-ui", "sans-serif"],
        display: ["Poppins", "Inter", "system-ui", "sans-serif"],
      },
      backdropBlur: { xs: "2px" },
    },
  },
  plugins: [],
};
