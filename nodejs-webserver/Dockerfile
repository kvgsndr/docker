FROM node:16
WORKDIR /app
#COPY package.json .
#COPY package-lock.json .
npm init
npm install --save express
RUN npm ci
COPY app.js .
CMD ["node", "app.js"]
