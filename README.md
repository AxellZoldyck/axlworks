# Axlworks

A creative software lab for digital systems, product interfaces, and interactive experiments.

## Stack

- Next.js 16
- React 19
- TypeScript
- Native CSS / React motion
- Docker with Next.js standalone output

## Run locally

```bash
npm install
npm run dev
```

Open `http://localhost:3000`.

## Deploy on a VPS

```bash
git clone https://github.com/AxellZoldyck/axlworks.git
cd axlworks
docker compose up -d --build
```

The container listens on port `3000`. Point your reverse proxy to `127.0.0.1:3000`.

For Caddy:

```text
axlworks.co {
    reverse_proxy 127.0.0.1:3000
}
```

Caddy can then handle HTTPS automatically.

## Design direction

Axlworks is intentionally not a conventional CV portfolio. The homepage is built around:

- an abstract motion frame
- cursor-driven parallax
- rotating orbital geometry
- hover-reactive project rows
- an experimental dark lab section
- responsive mobile composition
- reduced-motion support

Featured work currently includes Rentalin, XL SATU, and Kejar Target.

## Next layer

The structure is ready to expand with dedicated project pages, interactive case studies, a real experiment gallery, and more advanced canvas/WebGL scenes when they add value.
