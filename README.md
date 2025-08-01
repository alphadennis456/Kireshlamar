# KireshLamar Hybrid Bar System

Hybrid bar management built on Odoo 16:

- Pending Payment → Assign Products workflow
- M-Pesa sandbox + quick demo mode
- Preloaded bar products & dashboards
- Manager & Cashier demo users

## Setup (Render)

1. Fork repo → Deploy Web Service (Docker)
2. Create PostgreSQL DB (Render free tier)
3. Add environment variables:
   - DB_HOST
   - DB_NAME
   - DB_USER
   - DB_PASSWORD
   - DB_PORT
4. Redeploy → Login via Odoo APK

### Demo Users

- **Manager**: `manager@bar.com` / `manager123`  
- **Cashier**: `cashier@bar.com` / `cashier123`
