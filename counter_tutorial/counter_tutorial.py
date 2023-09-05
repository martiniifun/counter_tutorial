import reflex as rx


class State(rx.State):
    count_1_1: int = 0
    count_2_1: int = 0
    count_3_1: int = 0
    count_4_1: int = 0
    count_1_2: int = 0
    count_2_2: int = 0
    count_3_2: int = 0
    count_4_2: int = 0
    count_1_3: int = 0
    count_2_3: int = 0
    count_3_3: int = 0
    count_4_3: int = 0
    count_1_4: int = 0
    count_2_4: int = 0
    count_3_4: int = 0
    count_4_4: int = 0

    def increment_1_1(self):
        self.count_1_1 += 1

    def decrement_1_1(self):
        self.count_1_1 -= 1

    def increment_1_2(self):
        self.count_1_2 += 1

    def decrement_1_2(self):
        self.count_1_2 -= 1

    def increment_1_3(self):
        self.count_1_3 += 1

    def decrement_1_3(self):
        self.count_1_3 -= 1

    def increment_1_4(self):
        self.count_1_4 += 1

    def decrement_1_4(self):
        self.count_1_4 -= 1

    def increment_2_1(self):
        self.count_2_1 += 1

    def decrement_2_1(self):
        self.count_2_1 -= 1

    def increment_2_2(self):
        self.count_2_2 += 1

    def decrement_2_2(self):
        self.count_2_2 -= 1

    def increment_2_3(self):
        self.count_2_3 += 1

    def decrement_2_3(self):
        self.count_2_3 -= 1

    def increment_2_4(self):
        self.count_2_4 += 1

    def decrement_2_4(self):
        self.count_2_4 -= 1

    def increment_3_1(self):
        self.count_3_1 += 1

    def decrement_3_1(self):
        self.count_3_1 -= 1

    def increment_3_2(self):
        self.count_3_2 += 1

    def decrement_3_2(self):
        self.count_3_2 -= 1

    def increment_3_3(self):
        self.count_3_3 += 1

    def decrement_3_3(self):
        self.count_3_3 -= 1

    def increment_3_4(self):
        self.count_3_4 += 1

    def decrement_3_4(self):
        self.count_3_4 -= 1

    def increment_4_1(self):
        self.count_4_1 += 1

    def decrement_4_1(self):
        self.count_4_1 -= 1

    def increment_4_2(self):
        self.count_4_2 += 1

    def decrement_4_2(self):
        self.count_4_2 -= 1

    def increment_4_3(self):
        self.count_4_3 += 1

    def decrement_4_3(self):
        self.count_4_3 -= 1

    def increment_4_4(self):
        self.count_4_4 += 1

    def decrement_4_4(self):
        self.count_4_4 -= 1


def index():
    return rx.hstack(
        rx.vstack(
            rx.heading("참가자"),
            rx.heading("참가자A"),
            rx.heading("참가자B"),
            rx.heading("참가자C"),
            rx.heading("참가자D"),
        ),
        rx.spacer(),
        rx.vstack(
            rx.heading("사람"),
            rx.hstack(
                rx.button(
                    "-",
                    color_scheme="red",
                    border_radius="1em",
                    on_click=State.decrement_1_1,
                ),
                rx.heading(State.count_1_1, font_size="2em"),
                rx.button(
                    "+",
                    color_scheme="green",
                    border_radius="1em",
                    on_click=State.increment_1_1,
                ),
            ),
            rx.hstack(
                rx.button(
                    "-",
                    color_scheme="red",
                    border_radius="1em",
                    on_click=State.decrement_1_2,
                ),
                rx.heading(State.count_1_2, font_size="2em"),
                rx.button(
                    "+",
                    color_scheme="green",
                    border_radius="1em",
                    on_click=State.increment_1_2,
                ),
            ),
            rx.hstack(
                rx.button(
                    "-",
                    color_scheme="red",
                    border_radius="1em",
                    on_click=State.decrement_1_3,
                ),
                rx.heading(State.count_1_3, font_size="2em"),
                rx.button(
                    "+",
                    color_scheme="green",
                    border_radius="1em",
                    on_click=State.increment_1_3,
                ),
            ),
            rx.hstack(
                rx.button(
                    "-",
                    color_scheme="red",
                    border_radius="1em",
                    on_click=State.decrement_1_4,
                ),
                rx.heading(State.count_1_4, font_size="2em"),
                rx.button(
                    "+",
                    color_scheme="green",
                    border_radius="1em",
                    on_click=State.increment_1_4,
                ),
            ),
        ),
        rx.spacer(),
        rx.vstack(
            rx.heading("주제"),
            rx.hstack(
                rx.button(
                    "-",
                    color_scheme="red",
                    border_radius="1em",
                    on_click=State.decrement_2_1,
                ),
                rx.heading(State.count_2_1, font_size="2em"),
                rx.button(
                    "+",
                    color_scheme="green",
                    border_radius="1em",
                    on_click=State.increment_2_1,
                ),
            ),
            rx.hstack(
                rx.button(
                    "-",
                    color_scheme="red",
                    border_radius="1em",
                    on_click=State.decrement_2_2,
                ),
                rx.heading(State.count_2_2, font_size="2em"),
                rx.button(
                    "+",
                    color_scheme="green",
                    border_radius="1em",
                    on_click=State.increment_2_2,
                ),
            ),
            rx.hstack(
                rx.button(
                    "-",
                    color_scheme="red",
                    border_radius="1em",
                    on_click=State.decrement_2_3,
                ),
                rx.heading(State.count_2_3, font_size="2em"),
                rx.button(
                    "+",
                    color_scheme="green",
                    border_radius="1em",
                    on_click=State.increment_2_3,
                ),
            ),
            rx.hstack(
                rx.button(
                    "-",
                    color_scheme="red",
                    border_radius="1em",
                    on_click=State.decrement_2_4,
                ),
                rx.heading(State.count_2_4, font_size="2em"),
                rx.button(
                    "+",
                    color_scheme="green",
                    border_radius="1em",
                    on_click=State.increment_2_4,
                ),
            ),
        ),
        rx.spacer(),
        rx.vstack(
            rx.heading("행동"),
            rx.hstack(
                rx.button(
                    "-",
                    color_scheme="red",
                    border_radius="1em",
                    on_click=State.decrement_3_1,
                ),
                rx.heading(State.count_3_1, font_size="2em"),
                rx.button(
                    "+",
                    color_scheme="green",
                    border_radius="1em",
                    on_click=State.increment_3_1,
                ),
            ),
            rx.hstack(
                rx.button(
                    "-",
                    color_scheme="red",
                    border_radius="1em",
                    on_click=State.decrement_3_2,
                ),
                rx.heading(State.count_3_2, font_size="2em"),
                rx.button(
                    "+",
                    color_scheme="green",
                    border_radius="1em",
                    on_click=State.increment_3_2,
                ),
            ),
            rx.hstack(
                rx.button(
                    "-",
                    color_scheme="red",
                    border_radius="1em",
                    on_click=State.decrement_3_3,
                ),
                rx.heading(State.count_3_3, font_size="2em"),
                rx.button(
                    "+",
                    color_scheme="green",
                    border_radius="1em",
                    on_click=State.increment_3_3,
                ),
            ),
            rx.hstack(
                rx.button(
                    "-",
                    color_scheme="red",
                    border_radius="1em",
                    on_click=State.decrement_3_4,
                ),
                rx.heading(State.count_3_4, font_size="2em"),
                rx.button(
                    "+",
                    color_scheme="green",
                    border_radius="1em",
                    on_click=State.increment_3_4,
                ),
            ),
        ),
        rx.spacer(),
        rx.vstack(
            rx.heading("기타"),
            rx.hstack(
                rx.button(
                    "-",
                    color_scheme="red",
                    border_radius="1em",
                    on_click=State.decrement_4_1,
                ),
                rx.heading(State.count_4_1, font_size="2em"),
                rx.button(
                    "+",
                    color_scheme="green",
                    border_radius="1em",
                    on_click=State.increment_4_1,
                ),
            ),
            rx.hstack(
                rx.button(
                    "-",
                    color_scheme="red",
                    border_radius="1em",
                    on_click=State.decrement_4_2,
                ),
                rx.heading(State.count_4_2, font_size="2em"),
                rx.button(
                    "+",
                    color_scheme="green",
                    border_radius="1em",
                    on_click=State.increment_4_2,
                ),
            ),
            rx.hstack(
                rx.button(
                    "-",
                    color_scheme="red",
                    border_radius="1em",
                    on_click=State.decrement_4_3,
                ),
                rx.heading(State.count_4_3, font_size="2em"),
                rx.button(
                    "+",
                    color_scheme="green",
                    border_radius="1em",
                    on_click=State.increment_4_3,
                ),
            ),
            rx.hstack(
                rx.button(
                    "-",
                    color_scheme="red",
                    border_radius="1em",
                    on_click=State.decrement_4_4,
                ),
                rx.heading(State.count_4_4, font_size="2em"),
                rx.button(
                    "+",
                    color_scheme="green",
                    border_radius="1em",
                    on_click=State.increment_4_4,
                ),
            ),
        ),
    )


app = rx.App()
app.add_page(index)
app.compile()
