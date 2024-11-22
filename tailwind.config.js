/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html', // Matches all HTML files in templates and subdirectories
    './static_assets/**/*.js',      // Matches all JavaScript files in static and subdirectories
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

