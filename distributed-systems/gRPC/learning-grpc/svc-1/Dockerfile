FROM node:18-alpine

WORKDIR /app

# Copy package files
COPY svc-1/package.json svc-1/pnpm-lock.yaml ./

# Install pnpm and dependencies
RUN npm install -g pnpm
RUN pnpm install

# Install ts-node globally for development
RUN npm install -g ts-node typescript

# Copy source code
COPY svc-1/ .

# Copy proto files
COPY proto ./proto

# Command to run the application
CMD ["pnpm", "run", "dev"]
