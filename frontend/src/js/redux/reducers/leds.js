import { RECEIVE_LEDS } from '../actions/index';

const leds = (state = [], action) => {
    switch (action.type) {
        case RECEIVE_LEDS:
            return action.leds;

        default:
            return state;
    }
};

export default leds;