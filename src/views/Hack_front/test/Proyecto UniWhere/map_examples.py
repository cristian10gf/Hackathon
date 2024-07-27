import random
import flet as ft
import flet.map as map


def main(page: ft.Page):
    marker_layer_ref = ft.Ref[map.MarkerLayer]()
    circle_layer_ref = ft.Ref[map.CircleLayer]()

    def handle_tap(e: map.MapTapEvent):
        print(
            f"Name: {e.name} - coordinates: {e.coordinates} - Local: ({e.local_x}, {e.local_y}) - Global: ({e.global_x}, {e.global_y})"
        )
        if e.name == "tap":
            marker_layer_ref.current.markers.append(
                map.Marker(
                    content=
                    #ft.Image(
                    #    src="https://flet.dev/assets/flet-logo.png",
                    #    width=30,
                    #    height=30,
                    #),

                    
                    
                    
                    
                    ft.Icon(
                        ft.icons.LOCATION_ON, color=ft.cupertino_colors.DESTRUCTIVE_RED
                    ),
                    coordinates=e.coordinates,
                )
            )
        elif e.name == "secondary_tap":
            circle_layer_ref.current.circles.append(
                map.CircleMarker(
                    radius=random.randint(5, 10),
                    coordinates=e.coordinates,
                    color=ft.colors.random_color(),
                    border_color=ft.colors.random_color(),
                    border_stroke_width=4,
                )
            )
        page.update()

    def handle_event(e: map.MapEvent):
        print(
            f"{e.name} - Source: {e.source} - Center: {e.center} - Zoom: {e.zoom} - Rotation: {e.rotation}"
        )

    def on_keyboard(e: ft.KeyboardEvent):
        print(e.data)
        if e.key == "F" and e.ctrl:  # borrado de marcadores
            circle_layer_ref.current.circles.pop()
            page.update()

        if e.key == "D" and e.ctrl:
            # print(circle_layer_ref.current.circles[-1].coordinates)
            mapa.layers.append(
                map.PolygonLayer(
                    polygons=[
                        map.PolygonMarker(
                            label="area resaltada",
                            label_text_style=ft.TextStyle(
                                color=ft.colors.BLACK,
                                size=15,
                                weight=ft.FontWeight.BOLD,
                            ),
                            color=ft.colors.with_opacity(0.3, ft.colors.BLUE),
                            coordinates=[
                                map.MapLatitudeLongitude(
                                    circle_layer_ref.current.circles[
                                        -1
                                    ].coordinates.latitude,
                                    circle_layer_ref.current.circles[
                                        -1
                                    ].coordinates.longitude,
                                ),
                                map.MapLatitudeLongitude(
                                    circle_layer_ref.current.circles[
                                        -2
                                    ].coordinates.latitude,
                                    circle_layer_ref.current.circles[
                                        -2
                                    ].coordinates.longitude,
                                ),
                                map.MapLatitudeLongitude(
                                    circle_layer_ref.current.circles[
                                        -3
                                    ].coordinates.latitude,
                                    circle_layer_ref.current.circles[
                                        -3
                                    ].coordinates.longitude,
                                ),
                            ],
                        ),
                    ],
                )
            )
            page.update()

    page.on_keyboard_event = on_keyboard

    mapa = map.Map(
        # expand=True,
        height=320,
        width=320,
        # border_radius=10,
        configuration=map.MapConfiguration(
            initial_center=map.MapLatitudeLongitude(
                11.01914606845038, -74.85067043557093
            ),
            initial_zoom=18,
            interaction_configuration=map.MapInteractionConfiguration(
                flags=map.MapInteractiveFlag.ALL
            ),
            on_init=lambda e: print(f"Initialized Map"),
            on_tap=handle_tap,
            on_secondary_tap=handle_tap,
            on_long_press=handle_tap,
            on_event=handle_event,
        ),
        layers=[
            map.TileLayer(
                url_template="https://tile.openstreetmap.org/{z}/{x}/{y}.png",
                on_image_error=lambda e: print("TileLayer Error"),
            ),
            # map.RichAttribution(
            #     attributions=[
            #         map.TextSourceAttribution(
            #             text="OpenStreetMjjjap Contributors",
            #             on_click=lambda e: e.page.launch_url(
            #                 "https://openstreetmap.org/copyright"
            #             ),
            #         ),
            #         map.TextSourceAttribution(
            #             text="Flet",
            #             on_click=lambda e: e.page.launch_url("https://flet.dev"),
            #         ),
            #     ]
            # ),
            # map.SimpleAttribution(
            #     text="Flet",
            #     alignment=ft.alignment.top_right,
            #     on_click=lambda e: print("Clicked SimpleAttribution"),
            # ),
            map.MarkerLayer(
                ref=marker_layer_ref,
                markers=[
                    map.Marker(
                        content=ft.Icon(ft.icons.LOCATION_ON),
                        coordinates=map.MapLatitudeLongitude(30, 15),
                    ),
                    map.Marker(
                        content=ft.Icon(ft.icons.LOCATION_ON),
                        coordinates=map.MapLatitudeLongitude(10, 10),
                    ),
                    map.Marker(
                        content=ft.Icon(ft.icons.LOCATION_ON),
                        coordinates=map.MapLatitudeLongitude(25, 45),
                    ),
                ],
            ),
            map.CircleLayer(
                ref=circle_layer_ref,
                circles=[
                    map.CircleMarker(
                        radius=10,
                        coordinates=map.MapLatitudeLongitude(16, 24),
                        color=ft.colors.RED,
                        border_color=ft.colors.BLUE,
                        border_stroke_width=4,
                    ),
                ],
            ),
            map.PolygonLayer(
                polygons=[
                    map.PolygonMarker(
                        label="Popular Touristic Area",
                        label_text_style=ft.TextStyle(
                            color=ft.colors.BLACK,
                            size=15,
                            weight=ft.FontWeight.BOLD,
                        ),
                        color=ft.colors.with_opacity(0.3, ft.colors.BLUE),
                        coordinates=[
                            map.MapLatitudeLongitude(10, 10),
                            map.MapLatitudeLongitude(30, 15),
                            map.MapLatitudeLongitude(25, 45),
                            map.MapLatitudeLongitude(10, 45),
                        ],
                    ),
                ],
            ),
            map.PolylineLayer(
                polylines=[
                    map.PolylineMarker(
                        border_stroke_width=3,
                        border_color=ft.colors.RED,
                        gradient_colors=[ft.colors.BLACK, ft.colors.BLACK],
                        color=ft.colors.with_opacity(0.6, ft.colors.GREEN),
                        coordinates=[
                            map.MapLatitudeLongitude(10, 10),
                            map.MapLatitudeLongitude(30, 15),
                            map.MapLatitudeLongitude(25, 45),
                            map.MapLatitudeLongitude(10, 45),
                        ],
                    ),
                ],
            ),
        ],
    )

    map_base = ft.Container(
        content=mapa,
        alignment=ft.alignment.center,
        width=320,
        height=320,
        padding=0,
        bgcolor=ft.colors.TRANSPARENT,
        border_radius=10,
        border=ft.Border(
            top=ft.BorderSide(1, ft.colors.with_opacity(0, "#d9d9d9")),
            bottom=ft.BorderSide(1, ft.colors.with_opacity(0, "#d9d9d9")),
            left=ft.BorderSide(1, ft.colors.with_opacity(0, "#d9d9d9")),
            right=ft.BorderSide(1, ft.colors.with_opacity(0, "#d9d9d9")),
        ),
    )

    page.add(
        # ft.Text("Click anywhere to add a Marker, right-click to add a CircleMarker."),
        map_base
    )


ft.app(target=main)
