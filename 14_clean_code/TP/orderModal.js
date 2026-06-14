import { confirmOrder } from "../services/orderService.js";

export function renderOrderDetails(order) {

    const modal =
        document.getElementById("orderModal");

    const detailsDiv =
        modal.querySelector("#orderDetails");

    detailsDiv.innerHTML = "";

    detailsDiv.innerHTML = `
        <h3>Order ID: ${order.id}</h3>
        <p>Status: ${order.status}</p>
    `;
}

export function showModal() {
    document.getElementById(
        "orderModal"
    ).style.display = "block";
}

export function setupCloseButton() {

    const modal =
        document.getElementById("orderModal");

    modal.querySelector(".close").onclick =
        () => {
            modal.style.display = "none";
        };
}

export function setupConfirmButton(
    order,
    token
) {

    const confirmBtn =
        document.getElementById(
            "confirmOrderBtn"
        );

    if (order.status === "Delivered") {
        confirmBtn.style.display = "none";
        return;
    }

    confirmBtn.style.display = "block";

    confirmBtn.onclick = () => {
        confirmOrder(order.id, token);
    };
}