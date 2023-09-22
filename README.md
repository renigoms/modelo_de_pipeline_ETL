# Modelo_de_Pipeline_ETL
Desafio de projeto do santander bootcamp de ciência de dados com python da DIO

<h2>Introdução</h2>

* O desafio consistia em reimaginar o modelo ensinado no BootCamp da DIO.

* O funcionamento do programa é bem simples, ele extrai 3 registros de um banco de dados mysql a partir de uma lista de ids em csv manipulada com pandas e adiciona a cada um desse registros frase de motivação e bem-estar.

<h2>Ferramentas Necessárias</h2>

* Para que o programa funcione corretamente é necessário estabelecer uma conexão com um banco de dados mysql local com o wampserve caso der problema também é possível usar o xampp para a mesma finalidade.

* Ademais, é necessário que o dump seja importado para o workbench.

* Para concluir, também fiz uso das bibliotecas pandas e chatterbot, essa ultima presente aqui: https://github.com/ShoneGK/ChatterPy, pois comtém uma versão que funcionar na versão 3.11 do python ao qual usei.

* OBSERVAÇÃO: caso der algum problema com o spacy -> pip install spacy.

<table>
    <thead>
        <tr align="center">
            <th colspan=2>Banco de Dados MySql</th>
        </tr>
    </thead>
    <tbody align="left">
        <tr>
            <td>WorkBench</td>
            <td align="center">
                <a href="https://www.mysql.com/products/workbench/"><img src="https://logospng.org/download/mysql/mysql-256.png" alt="workbench" width=60px></a>
            </td>
        </tr>
        <tr>
            <td>WampServer</td>
            <td align="center">
                <a href="https://www.wampserver.com/en/">
                    <img src="https://ded9.com/wp-content/uploads/2022/11/Wampserver-software-for-pc.png" alt="" width=100px>
                </a>
            </td>
        </tr>
    </tbody>
    <tfoot></tfoot>
</table>


<br>

<h2>Exemplo de Funcionamento</h2>
<p>Como dar Run?</p>
<img align="center" src="imgReadMe/Captura de tela 2023-09-22 111053.png" alt="Run" >
<h3>EX1</h3>
    <img align="center" src="imgReadMe/Captura de tela 2023-09-22 111356.png" alt="EX1" >
<h3>EX2</h3>
     <img align="center" src="imgReadMe/Captura de tela 2023-09-22 111613.png" alt="EX2" >
<h3>EX3</h3>
     <img align="center" src="imgReadMe/Captura de tela 2023-09-22 112021.png" alt="EX3" >
