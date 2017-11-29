import { RECEIVE_LEDS, UPDATE_LED } from '../actions/index';

const leds = (state = [], action) => {
    switch (action.type) {
        case RECEIVE_LEDS:
            return action.leds;

        case UPDATE_LED:
            return state.map(s => {
                if (s.id === action.led.id) {
                    s.state = action.led.state;
                }
                return s;
            });

            return action.led;

        default:
            return state;
    }
};

export default leds;