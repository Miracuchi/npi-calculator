# choosed lts-alpine because it's lighter than non alpine
FROM node:lts-alpine 
WORKDIR /app
COPY package.json .
RUN npm i
COPY src src
COPY public public
COPY tsconfig.json .
COPY vite.config.ts .
COPY tsconfig.app.json .
COPY tsconfig.node.json .
COPY index.html .
COPY tailwind.config.js .
COPY postcss.config.cjs .
CMD npm run dev