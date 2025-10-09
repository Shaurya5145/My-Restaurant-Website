# sCODER Kitchen 🍴

sCODER Kitchen is a dynamic restaurant website built with **Python Django**. It allows users to explore the menu, view dishes, and provides an easy-to-manage backend for restaurant owners.

---

## Features

- **Menu Display:** Browse all available dishes with descriptions and prices.  
- **User Management:** Users can register, login, and manage profiles.  
- **Admin Panel:** Easily add, edit, or remove menu items through Django admin.  
- **Responsive Design:** Works well on both desktop and mobile devices.  
- **Media Handling:** Upload and display images for dishes.  

---

## Tech Stack

- **Backend:** Python Django  
- **Frontend:** HTML, CSS, JavaScript 
- **Database:** PostgreSQL  
- **Deployment:** Deployed on Azure

---

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Shaurya5145/My-Restaurant-Website.git
    cd sCODER-Kitchen
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate    # Linux/Mac
    venv\Scripts\activate       # Windows
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser (for admin access):**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7. **Open in browser:**  
    Visit `http://127.0.0.1:8000/`

---

## Usage

- Admin can manage dishes, categories, and orders from the Django admin panel.  
- Users can view dishes and interact with the website according to the implemented features.  

---

## Contributing

1. Fork the repository.  
2. Create a new branch: `git checkout -b feature-name`  
3. Make your changes and commit: `git commit -m "Description of changes"`  
4. Push to the branch: `git push origin feature-name`  
5. Open a Pull Request  

---

## License

This project is licensed under the MIT License.  

---

## Contact

- **Project Owner:** sCODER  
- **Email:** `gshaurya948@gmail.com`  
- **Website:** `https://scoder-restaurant.centralindia.cloudapp.azure.com/`
