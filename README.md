# 🎁 PresentPerfect — Your One-Stop Shop for Thoughtful Gifts

A focused, minimalistic e-commerce platform built with Django and Python to streamline online gift shopping by eliminating catalog clutter, complex multi-step checkouts, and promotional distractions.

---

## 📌 Project Overview

Traditional e-commerce platforms prioritize massive product catalogs and complex filtering systems, which often overwhelm users searching for specific, thoughtful gifts. PresentPerfect addresses decision fatigue by providing a niche, curated shopping environment. By prioritizing a clean layout, occasion-based categories, dynamic cart management, and a simplified checkout flow, the platform delivers an intuitive, distraction-free gift-buying experience.

---

## ✨ Key Features

* **Curated Gift Selection:** Focused catalog organized into dedicated categories (e.g., Luxury, Handmade, Chocolates, Fashion Accessories) to minimize decision fatigue.
* **Streamlined Single-Page Checkout:** Fast checkout experience designed without pop-ups, upsells, or promotional clutter.
* **Dynamic Shopping Cart:** Real-time item quantity adjustments, instant price calculations, and cart modifications.
* **Order & Inventory Synchronization:** Automated order generation linked with real-time inventory updates upon purchase completion.
* **User Authentication & History:** Secure registration and login handling with structured personal order tracking.

---

## 📁 Project Structure

```text
PresentPerfect/
│
├── manage.py                # Django CLI & project management script
├── db.sqlite3               # SQLite database instance
├── README.md                # Project documentation
│
├── presentperfect/          # Core project settings & configuration
│   ├── __init__.py
│   ├── settings.py          # App settings, DB connections, static configs
│   ├── urls.py              # Root URL routing table
│   └── wsgi.py              # WSGI server entry point
│
├── store/                   # Main application module
│   ├── __init__.py
│   ├── admin.py             # Django admin registration for items/orders
│   ├── apps.py              # Store app configuration
│   ├── models.py            # Database schemas (Products, Orders, Inventory)
│   ├── views.py             # Business logic & request handling
│   ├── urls.py              # Application-level endpoints
│   ├── templates/           # Server-side rendered HTML views
│   │   ├── home.html        # Main showcase (Pre & Post login views)
│   │   ├── login.html       # User authentication interface
│   │   ├── cart.html        # Dynamic shopping cart view
│   │   ├── orders.html      # User order history view
│   │   └── category.html    # Filtered category views
│   └── static/              # CSS stylesheets, JavaScript files, & images
│
└── assets/                  # Product imagery & documentation diagrams
