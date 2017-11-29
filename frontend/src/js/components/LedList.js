import React, { Component } from 'react'
import PropTypes from 'prop-types'
import Led from './Led';

export default class LedList extends Component{
    constructor(props) {
        super(props);
    }

    render() {
        return(
            <div>
                {this.props.leds.map(led => (
                    <Led
                        key={led.id}
                        id={led.id}
                        onLedChange={this.props.onChange}
                        state={!!led.state}
                    />
                ))}
            </div>
        );
    }
}

/*LedList.proptypes = {
    leds: PropTypes.arrayof
};*/