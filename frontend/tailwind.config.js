/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html", "./src/**/*.tsx", "./src/*.tsx"],
  theme: {
    extend: {
      fontFamily: {
        calculator: ["Calculator"],
      },
    },
  },
  plugins: [],
};
