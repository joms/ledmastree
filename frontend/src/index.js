import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { AppContainer } from 'react-hot-loader'
import App from './js/containers/app';

/*import configureStore from './js/redux/configureStore';

const store = configureStore();*/

const root = document.querySelector('#app');
ReactDOM.render(
    <AppContainer>
        <App/>
    </AppContainer>,
    root,
);

// Webpack Hot Module Replacement API
if (module.hot) {
    module.hot.accept('./js/containers/app', () => { render(App) })
}