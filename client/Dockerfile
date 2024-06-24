# Use the official Node.js image from the Docker Hub
FROM node:20.11.1

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json files into the container
COPY package.json package-lock.json ./

# Install any dependencies
RUN npm install

# Copy the current directory contents into the container
COPY . .

# Expose port 5173
EXPOSE 5173

# Run the development server
CMD ["npm", "run", "dev"]
