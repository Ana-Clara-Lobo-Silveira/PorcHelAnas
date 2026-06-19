// Função principal para buscar os dados do Flask e renderizar na tela
function atualizarCarrinhoVisual() {
    fetch('/meu_carrinho')
        .then(response => response.json())
        .then(itens => {
            const container = document.getElementById('cart-items');
            if (!container) return;
            
            container.innerHTML = ''; // Limpa o container para evitar duplicados

            if (itens.length === 0) {
                container.innerHTML = '<p class="cart-vazio">O seu carrinho está vazio.</p>';
                return;
            }

            // Mapeia e insere cada produto do banco de dados no HTML
            itens.forEach(item => {
                const divItem = document.createElement('div');
                divItem.classList.add('cart-item');

                divItem.innerHTML = `
                    <img src="/static/img/${item.imagem_produto}" alt="${item.nome_produto}" class="cart-item__img">
                    <div class="cart-item__details">
                        <p class="cart-item__name">${item.nome_produto}</p>
                        <p class="cart-item__price">R$ ${item.preco}</p>
                        <span class="cart-item__quantity">Qtd: ${item.quantidade}</span>
                    </div>
                `;

                container.appendChild(divItem);
            });
        })
        .catch(error => console.error('Erro ao buscar dados do carrinho:', error));
}

// Configuração dos botões de Abrir e Fechar a aba lateral
document.addEventListener('DOMContentLoaded', () => {
    // Busca os elementos na tela
    const cartSidebar = document.querySelector('.cart');
    const openBtn = document.querySelector('.header__toggle');
    const closeBtn = document.getElementById('close-cart'); // Alvo para o 'X'

    // Abre o carrinho ao clicar no ícone do cabeçalho
    if (openBtn && cartSidebar) {
        openBtn.addEventListener('click', () => {
            cartSidebar.classList.add('active'); // Ativa a classe do CSS
            atualizarCarrinhoVisual(); // Carrega os dados atualizados do banco
        });
    }

    // Fecha o carrinho ao clicar no botão 'X'
    if (closeBtn && cartSidebar) {
        closeBtn.addEventListener('click', () => {
            cartSidebar.classList.remove('active'); // Remove a classe do CSS
        });
    }

    // Carrega os itens inicialmente se o carrinho já começar aberto
    atualizarCarrinhoVisual();
});