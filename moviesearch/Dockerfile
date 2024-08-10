# Use the official Node.js image.
FROM node:18

# Set the working directory.
WORKDIR /app

# Copy package.json and package-lock.json.
COPY package*.json ./

# Install dependencies.
RUN npm install

# Copy the rest of the application code.
COPY . .

# Build the React application.
RUN npm run build

# Serve the app with a static file server.
RUN npm install -g serve
CMD ["serve", "-s", "build"]

# Expose the port the app runs on.
EXPOSE 5000
EXPOSE 3000

# Start the application.
CMD ["serve", "-s", "build"]
