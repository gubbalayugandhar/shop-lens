-- Create Hotels table
CREATE TABLE Hotels (
    hotel_id INT PRIMARY KEY,
    hotel_name VARCHAR(255),
    location VARCHAR(255),
    rating FLOAT
);

-- Create Menus table
CREATE TABLE Menus (
    menu_id INT PRIMARY KEY,
    hotel_id INT,
    menu_name VARCHAR(255),
    FOREIGN KEY (hotel_id) REFERENCES Hotels(hotel_id)
);

-- Create Food Items table
CREATE TABLE FoodItems (
    food_item_id INT PRIMARY KEY,
    food_item_name VARCHAR(255),
    price DECIMAL(10, 2)
);

-- Create MenuFoodItems junction table
CREATE TABLE MenuFoodItems (
    menu_id INT,
    food_item_id INT,
    quantity INT,
    FOREIGN KEY (menu_id) REFERENCES Menus(menu_id),
    FOREIGN KEY (food_item_id) REFERENCES FoodItems(food_item_id),
    PRIMARY KEY (menu_id, food_item_id)  -- Composite primary key to handle many-to-many relationship
);
