# main.py

import flet as ft
import time
from DFA import nic_dfa


def main(page: ft.Page):
    page.title = "NIC DFA Validator"
    page.window_width = 900
    page.window_height = 600,
    page.scroll = "auto"

    nic_input = ft.TextField(
        label="Enter NIC Number",
        width=300
    )

    result_text = ft.Text(
        "",
        size=40,
        weight="bold"
    )

    table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Step", weight="bold")),
            ft.DataColumn(ft.Text("Input", weight="bold")),
            ft.DataColumn(ft.Text("From State", weight="bold")),
            ft.DataColumn(ft.Text("To State", weight="bold")),
        ],
        rows=[]
    )

    def validate_clicked(e):
        table.rows.clear()
        result_text.value = ""
        page.update()

        steps, final_state = nic_dfa(nic_input.value)

        for s in steps:
            table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(s["step"]))),
                        ft.DataCell(ft.Text(s["input"])),
                        ft.DataCell(ft.Text(s["from"])),
                        ft.DataCell(ft.Text(s["to"])),
                    ]
                )
            )
            page.update()
            time.sleep(0.75)   # step-by-step delay

        if final_state == "ACCEPT":
            result_text.value = "✅ ACCEPTED – Valid NIC"
            result_text.color = "green"
        else:
            result_text.value = "❌ REJECTED – Invalid NIC"
            result_text.color = "red"

        page.update()

    validate_btn = ft.ElevatedButton(
        "Validate NIC",
        on_click=validate_clicked,
        width=150,
        bgcolor=ft.Colors.BLUE_200,
        color=ft.Colors.BLACK
    )
    
    validate_btn.font_size = 30

    page.add(
        ft.Row(
            controls=[ft.Text("Sri Lankan NIC DFA Validator", size=50, weight="bold")],
            alignment=ft.MainAxisAlignment.CENTER,
            height=100,
        ),
        
        ft.Row(
             controls=[ft.Text("Developed By: Sehara Arunodya Fernando | 225513L", size=20, weight="semibold",color="grey")],
            alignment=ft.MainAxisAlignment.CENTER,
            height=30,
        ),
        
        ft.Row(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            nic_input,
                            validate_btn
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=20,
                    ),
                    width=1500,
                    padding=ft.padding.all(20),
                )
            ]
        ),
        
        ft.Row(
            [
                
                ft.Container(
                    content=ft.Column(
                        [
                            table
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=20,
                    ),
                    width=750,
                    padding=ft.padding.all(20),
                ),
                ft.Container(
                    content=ft.Column(
                        [
                            result_text
                        ],
                        spacing=20,
                    ),
                    alignment=ft.alignment.top_center,
                    width=750
                ),
                
            ]
        )
        # ft.Column(
        #         [
        #             nic_input,
        #             validate_btn,
        #         ],
        #         spacing=20,
        #     ),
        # ft.Column(
        #     [table],
        #     alignment=ft.MainAxisAlignment.START,
        #     scroll="auto",
        # ),
        
        # ft.Column()

        # ft.Row(
            
        # )
        # ft.Column(
        #     [
                
        #         nic_input,
        #         validate_btn,
        #         table,
        #         result_text
        #     ],
        #     spacing=20
        # )
    )


ft.app(target=main)
