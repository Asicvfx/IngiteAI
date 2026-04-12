# IngiteAI

IngiteAI is an AI-powered business automation platform for creating customer-facing assistants backed by your own business knowledge.

The product combines:
- a Nuxt dashboard for business owners
- a Django backend with APIs, auth, bot management, and knowledge storage
- OpenAI-powered response generation
- multi-channel bot delivery through Telegram and WhatsApp

The core idea is simple: a business uploads FAQs, policies, product documents, or raw text, and IngiteAI uses that information to generate useful customer replies in real time.

## What The Product Does

IngiteAI lets a business owner:
- create and manage AI bots
- upload a knowledge base as text or files
- connect messaging channels
- review conversations
- monitor activity in the dashboard
- authenticate with email/password or Google OAuth

Typical use cases:
- support bots for online stores
- lead qualification assistants
- FAQ bots for service businesses
- product consultation bots
- WhatsApp or Telegram assistants for small and mid-sized businesses

## Current Product Capabilities

At the moment, the project includes:
- user authentication with JWT-based API auth
- Google OAuth login
- bot creation and management
- knowledge base entries stored per bot
- text/file knowledge ingestion
- AI-generated responses using OpenAI
- Telegram webhook support
- WhatsApp Cloud API webhook support
- conversation and message persistence
- dashboard UI for managing bots and knowledge

## High-Level Architecture

IngiteAI is built as a modular monolith:
- `frontend/` contains the product UI
- `backend/` contains the API, auth, AI orchestration, and integrations

Request flow at a high level:
1. A user sends a message through Telegram or WhatsApp.
2. The backend receives the webhook event.
3. The backend loads recent conversation history and the bot's knowledge items.
4. The OpenAI service builds a system prompt plus knowledge context.
5. OpenAI returns a structured JSON response.
6. The backend stores the message and sends the reply back to the channel.

For dashboard usage:
1. The frontend calls Django REST API endpoints.
2. Auth is handled with `dj-rest-auth` and JWT.
3. Business owners create bots, upload knowledge, and monitor activity.

## Tech Stack

### Frontend
- Nuxt 3 / Nuxt 4-style app structure
- Vue 3
- Pinia
- Tailwind CSS
- Chart.js
- Vue Chart.js

Main frontend responsibilities:
- authentication flows
- dashboard pages
- bot management UI
- knowledge base upload and editing
- overview and analytics screens

### Backend
- Django
- Django REST Framework
- dj-rest-auth
- django-allauth
- Simple JWT
- Channels
- Daphne
- WhiteNoise

Main backend responsibilities:
- authentication and user management
- API endpoints for frontend
- bot management
- knowledge storage and parsing
- webhook processing for Telegram and WhatsApp
- AI response generation
- chat and message persistence

### Database
- PostgreSQL in production
- SQLite fallback for local development

### File Parsing / Knowledge Ingestion
- `pdfplumber` for PDF extraction
- `openpyxl` for Excel parsing
- plain text parsing for `.txt`

### External Integrations
- OpenAI API
- Telegram Bot API
- WhatsApp Cloud API
- Google OAuth

## AI Layer

The AI orchestration currently lives in:
- [backend/bots/services.py](</c:/Users/Asylzhan/Desktop/all startapp efforts/MYSTARTAPP-VelorAI/IngiteAI.V2/IngiteAI/backend/bots/services.py:1>)

### OpenAI Usage

The backend uses the official OpenAI Python SDK:
- package: `openai>=1.50.0`
- API key source: `OPENAI_API_KEY` environment variable

The current implementation uses:
- `gpt-4o` for chat response generation
- `whisper-1` for audio transcription

Important note:
- the repository should never contain a real OpenAI key
- only the environment variable name `OPENAI_API_KEY` should be documented and used

### How AI Responses Work

When generating a response, the backend:
- builds a system prompt that defines the assistant behavior
- injects knowledge base content into context
- injects recent conversation history
- optionally includes image input
- requests a structured JSON response from OpenAI

The expected response shape includes:
- `answer`
- `needs_human`
- `booking_requested`
- `booking_details`
- `lead_type`
- `products`
- `quick_replies`

This structure is useful because it supports more than plain text. It allows the product to evolve into:
- lead scoring
- booking flows
- product cards
- suggested next actions

## Knowledge Base System

The knowledge system is a key part of the product.

Relevant files:
- [backend/bots/models.py](</c:/Users/Asylzhan/Desktop/all startapp efforts/MYSTARTAPP-VelorAI/IngiteAI.V2/IngiteAI/backend/bots/models.py:1>)
- [backend/bots/services_knowledge.py](</c:/Users/Asylzhan/Desktop/all startapp efforts/MYSTARTAPP-VelorAI/IngiteAI.V2/IngiteAI/backend/bots/services_knowledge.py:1>)
- [frontend/pages/faq.vue](</c:/Users/Asylzhan/Desktop/all startapp efforts/MYSTARTAPP-VelorAI/IngiteAI.V2/IngiteAI/frontend/pages/faq.vue:1>)

Each bot can have many `KnowledgeItem` records.

Supported knowledge item types:
- `faq`
- `text`
- `file`

Supported file parsing right now:
- `.pdf`
- `.xlsx`
- `.xls`
- `.txt`

Current behavior:
- when a file is uploaded, the backend extracts text from it
- extracted content is stored and later injected into the model prompt
- the AI is instructed to answer from knowledge first and escalate when the answer is missing

This means IngiteAI is currently a prompt-context knowledge system, not a vector database / RAG pipeline yet.

## Authentication

Auth stack:
- Django auth
- `dj-rest-auth`
- `django-allauth`
- JWT authentication
- Google OAuth

Frontend auth logic:
- [frontend/stores/auth.ts](</c:/Users/Asylzhan/Desktop/all startapp efforts/MYSTARTAPP-VelorAI/IngiteAI.V2/IngiteAI/frontend/stores/auth.ts:1>)

Backend auth config:
- [backend/config/settings.py](</c:/Users/Asylzhan/Desktop/all startapp efforts/MYSTARTAPP-VelorAI/IngiteAI.V2/IngiteAI/backend/config/settings.py:1>)
- [backend/config/urls.py](</c:/Users/Asylzhan/Desktop/all startapp efforts/MYSTARTAPP-VelorAI/IngiteAI.V2/IngiteAI/backend/config/urls.py:1>)
- [backend/users/views.py](</c:/Users/Asylzhan/Desktop/all startapp efforts/MYSTARTAPP-VelorAI/IngiteAI.V2/IngiteAI/backend/users/views.py:1>)

Supported auth flows:
- email/username + password
- Google sign-in
- authenticated API access from the dashboard

## Messaging Channels

### Telegram

Telegram support is handled through:
- bot tokens stored in the database
- webhook registration
- webhook message processing
- outbound `sendMessage` calls

Relevant service code:
- [backend/bots/services.py](</c:/Users/Asylzhan/Desktop/all startapp efforts/MYSTARTAPP-VelorAI/IngiteAI.V2/IngiteAI/backend/bots/services.py:111>)

### WhatsApp

WhatsApp support is implemented through WhatsApp Cloud API fields on the bot model and dedicated webhook handlers.

Relevant files:
- [backend/bots/views_whatsapp.py](</c:/Users/Asylzhan/Desktop/all startapp efforts/MYSTARTAPP-VelorAI/IngiteAI.V2/IngiteAI/backend/bots/views_whatsapp.py:1>)
- [backend/bots/models.py](</c:/Users/Asylzhan/Desktop/all startapp efforts/MYSTARTAPP-VelorAI/IngiteAI.V2/IngiteAI/backend/bots/models.py:1>)

## Project Structure

```text
IngiteAI/
├── backend/
│   ├── bots/              # Bot models, AI services, knowledge handling, channel integrations
│   ├── chats/             # Conversations, messages, chat persistence
│   ├── dashboard/         # Dashboard/admin-related backend logic
│   ├── meetings/          # Meeting or booking-related logic
│   ├── users/             # Users, businesses, auth-related views/serializers
│   ├── config/            # Django settings, urls, ASGI/WSGI config
│   ├── manage.py          # Django CLI entrypoint
│   ├── requirements.txt   # Python dependencies
│   └── Dockerfile         # Container startup config
├── frontend/
│   ├── pages/             # Product pages and dashboard routes
│   ├── components/        # Reusable UI components
│   ├── layouts/           # Shared page layouts
│   ├── stores/            # Pinia stores
│   ├── middleware/        # Auth and route middleware
│   ├── assets/            # Styles and static assets
│   ├── public/            # Public files
│   ├── nuxt.config.ts     # Frontend runtime config
│   └── package.json       # JS dependencies and scripts
└── README.md
```

## Environment Variables

Only variable names are documented here. Never commit real secrets.

### Backend `.env`

Typical backend environment variables:

```ini
DEBUG=False
SECRET_KEY=your_django_secret_key
ALLOWED_HOSTS=localhost,127.0.0.1,.onrender.com,ingiteai.online,www.ingiteai.online

PROJECT_URL=https://your-backend-domain
FRONTEND_URL=https://your-frontend-domain

CORS_ALLOWED_ORIGINS=https://your-frontend-domain
CSRF_TRUSTED_ORIGINS=https://your-frontend-domain

DATABASE_URL=postgresql://...

OPENAI_API_KEY=sk-...

GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret

EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_app_password
```

### Frontend `.env`

```ini
NUXT_PUBLIC_API_BASE=https://your-backend-domain
NUXT_PUBLIC_GOOGLE_CLIENT_ID=your_google_client_id
```

## Local Development

### Prerequisites
- Python 3.10+
- Node.js 18+
- npm

### Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Backend will run on:
- `http://localhost:8000`

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend will run on:
- `http://localhost:3000`

## Deployment

### Backend Deployment

The backend is designed for a Render-style deployment.

Important production pieces:
- `DATABASE_URL` for PostgreSQL
- `OPENAI_API_KEY`
- Google OAuth env vars
- CORS / CSRF trusted origins

The project includes:
- `gunicorn`
- `daphne`
- `whitenoise`

Current container/startup patterns indicate the backend is intended to:
- run migrations on startup
- create or prepare admin bootstrap tasks
- serve the ASGI/Django app

### Frontend Deployment

The frontend is suitable for Vercel deployment with:
- Nuxt build pipeline
- public runtime config for API base URL
- public Google client ID

## Important Implementation Notes

### What AI Model Is Used?

Current code uses:
- `gpt-4o` for text and multimodal response generation
- `whisper-1` for audio transcription

If you change the model later, update:
- [backend/bots/services.py](</c:/Users/Asylzhan/Desktop/all startapp efforts/MYSTARTAPP-VelorAI/IngiteAI.V2/IngiteAI/backend/bots/services.py:24>)

### What OpenAI Key Is Used?

The project uses the environment variable:
- `OPENAI_API_KEY`

The real key must live only in:
- local `.env`
- Render environment variables
- other secret managers

It should never be hardcoded in the repository or documentation.

### Is This RAG?

Not yet in the strict retrieval-augmented generation sense.

Right now the architecture is:
- upload knowledge
- extract text
- store knowledge in DB
- inject knowledge directly into the prompt

That is a prompt-injection knowledge architecture. It works for MVPs and small knowledge volumes, but later the project could evolve into:
- embeddings
- vector search
- chunk ranking
- retrieval pipeline
- source-grounded answers

### Current Strengths
- fast MVP architecture
- full-stack ownership in one repo
- easy knowledge injection
- direct business use case
- multi-channel potential

### Current Limitations
- no vector database / semantic retrieval yet
- large knowledge bases may become expensive or noisy in prompts
- AI prompt logic is still centralized in a single service layer
- pricing/lead routing/business rules are mostly prompt-driven

## Recommended Next Improvements

Good next steps for the product:
- split AI orchestration into clearer service layers
- add source attribution for knowledge answers
- introduce chunking + embeddings for larger knowledge bases
- add admin logs and observability around AI failures
- add tests around webhook handling and auth flows
- add per-bot prompt customization
- add guardrails for product pricing and stock confirmation

## Summary

IngiteAI is a real AI SaaS-style product for business messaging automation.

Its current architecture is:
- Nuxt frontend
- Django/DRF backend
- PostgreSQL-compatible persistence
- OpenAI-powered answer generation
- bot-specific knowledge base injection
- Telegram and WhatsApp channel support

It is already strong as an MVP and is structured well enough to keep growing into a more advanced AI assistant platform.
