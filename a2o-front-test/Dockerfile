# Use an official Node.js runtime as the base image
FROM node:18.16.0

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the entire project to the container
COPY . .

# Build the React app
RUN npm run build

# Specify the command to run when the container starts
CMD ["npm", "start"]
