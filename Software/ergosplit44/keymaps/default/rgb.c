#include "quantum.h"


bool rgb_matrix_indicators_advanced_user(uint8_t led_min, uint8_t led_max) {
    if (host_keyboard_led_state().caps_lock) {
        rgb_matrix_set_color(0, RGB_RED);
    } else {
        rgb_matrix_set_color(0, RGB_GREEN);
    }
    return false;
}
