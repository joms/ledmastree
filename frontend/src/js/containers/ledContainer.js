import React, { Component } from 'react';
import PropTypes from 'prop-types';

import Led from '../components/led';


class LedContainer extends Component {
    componentDidMount() {
        console.log(this.props);
    }

    render() {
        const { leds } = this.props;

        return (
            <div>
                {leds.map(led => (
                    <Led key={led.id} led={led}/>
                ))}
            </div>
        );
    }
}

export default LedContainer;