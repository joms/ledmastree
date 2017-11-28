import axios from 'axios';

export const REQUEST_LEDS = 'REQUEST_LEDS';
export const RECEIVE_LEDS = 'RECEIVE_LEDS';

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

export function fetchLeds() {
    return dispatch => {
        dispatch(requestLeds());
        return axios.get('http://192.168.3.10:5000/ledmastree/api/v1/leds')
            .then(response => response.data)
            .then(json => dispatch(receiveLeds(json)));
    }
}