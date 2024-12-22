import turtle

def draw_neon_text(text, x, y):
    # Set the turtle speed and pen size
    turtle.speed(0)
    turtle.pensize(5)

    # Define neon colors
    neon_colors = ["cyan", "magenta", "blue", "purple", "pink"]

    # Draw the text multiple times with different colors and offsets
    for i in range(10):
        turtle.penup()
        turtle.goto(x + i * 2, y - i * 2)  # Offset for neon effect
        turtle.pendown()
        turtle.color(neon_colors[i % len(neon_colors)])
        turtle.write(text, font=("Arial", 48, "bold"))

def main():
    # Set up the turtle screen
    turtle.bgcolor("black")  # Background color
    turtle.title("Neon Text Effect")

    # Draw the neon text
    draw_neon_text("CHANGE @ HERE", 0, 0)

    # Hide the turtle and finish
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
