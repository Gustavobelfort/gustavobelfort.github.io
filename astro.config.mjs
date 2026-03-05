import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://gustavo.belfort.dev',
  output: 'static',
  build: {
    assets: '_astro',
  },
});
