/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './node_modules/flowbite/**/*.js'
  ],
  future: {
    removeDeprecatedGapUtilities: true,
    purgeLayersByDefault: true,
  },
  purge: {
    enabled: false,
    content: ['../**/templates/*.html', '../**/templates/**/*.html'],
  },
  theme: {
    extend: {
    },
  },
  variants: {},
  plugins: [
    require('flowbite/plugin')
  ],
}