import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { AppContainer } from 'react-hot-loader'
import App from './js/containers/app';

import configureStore from './js/redux/configureStore';

const store = configureStore(
    window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__(),
);

const root = document.querySelector('#app');
ReactDOM.render(
    <Provider store={store}>
        <AppContainer>
            <App />
        </AppContainer>
    </Provider>,
    root,
);

// Webpack Hot Module Replacement API
if (module.hot) {
    module.hot.accept('./js/containers/app', () => { render(App) })
}