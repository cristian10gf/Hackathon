import random
import flet as ft
import flet.map as map
from flet import Geolocator


async def main(page: ft.Page):
    page.window.always_on_top = True
    page.on_error = lambda e: print(f"Page Error: {e.data}")
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.appbar = ft.AppBar(title=ft.Text("Geolocator Tests"))
    gl = Geolocator()
    page.overlay.append(gl)
    page.session.set("Mapa_exist", False)
    settings_dlg = lambda handler: ft.AlertDialog(
        adaptive=True,
        title=ft.Text("Opening Location Settings..."),
        content=ft.Text(
            "You are about to be redirected to the location/app settings. "
            "Please locate this app and grant it location permissions."
        ),
        actions=[
            ft.TextButton(
                text="OK",
                on_click=handler,
            ),
        ],
        actions_alignment=ft.MainAxisAlignment.CENTER,
    )

    def handle_permission_request(e):
        # print("d")
        page.add(ft.TextField(f"Pedir permisos: {gl.request_permission()}"))

    def handle_get_permission_status(e):
        # print("d")
        page.add(ft.TextField(f"Estado de los permisos: {gl.get_permission_status()}"))

    def handle_get_current_position(e):
        if page.session.get("Mapa_exist") == False:
            page.session.set("Mapa_exist", True)
        else:
            page.controls.pop()
            page.controls.pop()

        p = gl.get_current_position()
        lat = p.latitude
        lon = p.longitude
        page.add(
            ft.Container(
                content=map.Map(
                    # expand=True,
                    height=320,
                    width=320,
                    # border_radius=10,
                    configuration=map.MapConfiguration(
                        initial_center=map.MapLatitudeLongitude(
                            # 11.01914606845038, -74.85067043557093
                            lat,
                            lon,
                        ),
                        initial_zoom=18,
                        min_zoom=16.5,
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
                        map.MarkerLayer(
                            ref=marker_layer_ref,
                            markers=[
                                map.Marker(
                                    content=ft.Image(
                                        src=r"C:\Users\flavi\OneDrive\Escritorio\Hackaton_UniWhere\UniWhere_Front_End\Uniwhere_front\assets\images\Nao_nao.png",
                                        fit=ft.ImageFit.CONTAIN,
                                        height=60,
                                        width=80,
                                        repeat=ft.ImageRepeat.NO_REPEAT,
                                        border_radius=ft.border_radius.all(10),
                                        opacity=0.9,
                                    ),
                                    # ft.Icon(ft.icons.LOCATION_ON),
                                    height=60,
                                    width=80,
                                    coordinates=map.MapLatitudeLongitude(
                                        lat, lon + 0.0001
                                    ),
                                ),
                            ],
                        ),
                        map.CircleLayer(
                            ref=circle_layer_ref,
                            circles=[
                                map.CircleMarker(
                                    radius=6,
                                    coordinates=map.MapLatitudeLongitude(lat, lon),
                                    color=ft.colors.CYAN,
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
                ),
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
            ),
            ft.TextField(f"get_current_position: ({p.latitude}, {p.longitude})"),
        )
        page.update()

    def handle_get_last_known_position(e):
        p = gl.get_last_known_position()
        page.add(
            ft.TextField(f"get_last_known_position: ({p.latitude}, {p.longitude})")
        )

    def handle_location_service_enabled(e):
        page.add(
            ft.Text(f"is_location_service_enabled: {gl.is_location_service_enabled()}")
        )

    def handle_open_location_settings(e):
        page.close_dialog()
        page.add(ft.Text(f"open_location_settings: {gl.open_location_settings()}"))

    def handle_open_app_settings(e):
        page.close_dialog()
        page.add(ft.Text(f"open_app_settings: {gl.open_app_settings()}"))

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
                    # ft.Image(
                    #    src="https://flet.dev/assets/flet-logo.png",
                    #    width=30,
                    #    height=30,
                    # ),
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

    page.add(
        ft.Row(
            [
                ft.OutlinedButton(
                    "request_permission",
                    on_click=handle_permission_request,
                ),
                ft.OutlinedButton(
                    "get_permission_status",
                    on_click=handle_get_permission_status,
                ),
                ft.OutlinedButton(
                    "get_current_position",
                    on_click=handle_get_current_position,
                ),
                ft.OutlinedButton(
                    "get_last_known_position",
                    visible=False if page.web else True,
                    on_click=handle_get_last_known_position,
                ),
                ft.OutlinedButton(
                    "is_location_service_enabled",
                    on_click=handle_location_service_enabled,
                ),
                ft.OutlinedButton(
                    "open_location_settings",
                    visible=False if page.web else True,
                    on_click=lambda e: page.show_dialog(
                        settings_dlg(handle_open_location_settings)
                    ),
                ),
                ft.OutlinedButton(
                    "open_app_settings",
                    visible=False if page.web else True,
                    on_click=lambda e: page.show_dialog(
                        settings_dlg(handle_open_app_settings)
                    ),
                ),
            ],
            wrap=True,
        ),
    )


ft.app(main)
