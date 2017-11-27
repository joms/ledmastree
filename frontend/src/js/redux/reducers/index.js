import { combineReducers } from 'redux';
import leds from './leds';

const ledController = combineReducers({
    leds,
});

export default ledController;