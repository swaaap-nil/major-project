# Use an official Node.js image as base
FROM node:20-slim

# Set working directory
WORKDIR /app

# Install pnpm globally
RUN npm install -g pnpm


COPY . .


RUN pnpm install
EXPOSE 5173
# Default command (you can change this)
CMD ["pnpm", "dev"]
