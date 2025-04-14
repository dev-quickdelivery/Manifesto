document.addEventListener("DOMContentLoaded", function () {
  const btn = document.getElementById("btn-verificar");
  let etapa = "verificar"; // controla o fluxo

  btn.addEventListener("click", function () {
    const cpf = document.getElementById("cpf").value;
    const csrf = document.querySelector('[name=csrfmiddlewaretoken]').value;

    if (etapa === "verificar") {
      fetch("/verificar-cpf/", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
          "X-CSRFToken": csrf
        },
        body: new URLSearchParams({ cpf })
      })
        .then(res => res.json())
        .then(data => {
          console.log(data);

          if (data.status === 'tem_usuario') {
            document.getElementById('cpf').readOnly = true;
            document.querySelector('.text-center').innerText = 'Use sua senha para efetuar login';
            document.getElementById('senha-login').style.display = 'block';
            document.getElementById('primeiro-acesso').style.display = 'none';
            btn.innerText = 'Entrar';
            etapa = "login";
          } else if (data.status === 'sem_usuario') {
            document.getElementById('cpf').readOnly = true;
            document.querySelector('.text-center').innerText = 'Você ainda não tem uma senha cadastrada';
            document.getElementById('senha-login').style.display = 'none';
            document.getElementById('primeiro-acesso').style.display = 'block';
            btn.innerText = 'Cadastrar';
            
            etapa = "cadastro";
          } else {
            alert('CPF não encontrado.');
          }
        })
        .catch(err => console.error("Erro:", err));

    } else if (etapa === "login") {
      document.getElementById("form-login").submit(); // envia form padrão para login

    } else if (etapa === "cadastro") {
      const novaSenha = document.getElementById("nova_senha").value;
      const confirmarSenha = document.getElementById("confirmar_senha").value;

      if (novaSenha !== confirmarSenha) {
        alert("As senhas não coincidem.");
        return;
      }

      fetch("/primeiro-acesso/", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
          "X-CSRFToken": csrf
        },
        body: new URLSearchParams({
          cpf: cpf,
          senha: novaSenha
        })
      })
        .then(res => res.json())
        .then(data => {
          if (data.status === "ok") {
            alert("Senha cadastrada com sucesso!");
            location.reload(); // ou redireciona para login
          } else {
            alert("Erro ao cadastrar. Tente novamente.");
          }
        })
        .catch(err => console.error("Erro:", err));
    }
  });
});
