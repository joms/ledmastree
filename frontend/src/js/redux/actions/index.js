import axios from 'axios';

export const REQUEST_LEDS = 'REQUEST_LEDS';
export const UPDATE_LED = 'UPDATE_LED';
export const RECEIVE_LEDS = 'RECEIVE_LEDS';
export const RECEIVE_LED = 'RECEIVE_LED';

export function requestLeds() {
    return {
        type: REQUEST_LEDS,
    };
}

export function receiveLeds(json) {
    return {
        type: RECEIVE_LEDS,
        leds: json,
    };
}

export function updateLed(json) {
    return {
        type: UPDATE_LED,
        led: json
    };
}

export function fetchLeds() {
    return dispatch => {
        dispatch(requestLeds());
        return axios.get('ledmastree/api/v1/leds')
            .then(response => response.data)
            .then(json => dispatch(receiveLeds(json)));
    }
}

export function setLedState(id, state) {
    return dispatch => {
        return axios.get(`/ledmastree/api/v1/${state ? 'on' : 'off'}/${id}`)
            .then(response => response.data)
            .then(json => dispatch(updateLed(json)));
    }
}