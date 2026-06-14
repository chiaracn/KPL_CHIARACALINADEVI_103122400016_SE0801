import {
    getOrderDetails
} from "./api/orderApi.js";

import {
    renderOrderDetails,
    setupCloseButton,
    setupConfirmButton,
    showModal
} from "./ui/orderModal.js";

export async function fetchOrderDetails(
    orderId,
    token
) {

    try {

        const order =
            await getOrderDetails(
                orderId,
                token
            );

        renderOrderDetails(order);

        setupCloseButton();

        setupConfirmButton(
            order,
            token
        );

        showModal();

    } catch (error) {

        console.error(error);

    }
}