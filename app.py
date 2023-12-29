from shiny import App, ui

# Part 1: ui ----
app_ui = ui.page_fluid(
    ui.input_slider("n", "Choose a number n:", 0, 100, 50 ),
    ui.output_text_verbatim("txt")
)

# Part 2: server ----
def server(input, output, session):
    ...

# Combine into a shiny app.
# Note that the variable must be "app".
app = App(app_ui, server)
