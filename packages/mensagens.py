# Mensagens que serão utilizadas ao longo da aplicação.

menu = """
Os itens armazenados no estoque possuem um ID, nome, preço e quantidade. <br />
Para checar o conteudo atual do estoque, clique aqui: <a href="/checa_db">MOSTRAR ESTOQUE</a> <br />
Para adicionar um item no estoque, clique aqui: <a href="/adiciona_item">ADICIONAR ITEM</a> <br />
Para atualizar um item no estoque, clique aqui: <a href="/atualiza_item">ATUALIZAR ITEM</a> <br />
Para remover um item do estoque, clique aqui: <a href="/remove_item">REMOVER ITEM</a> <br />
<br /> <br />
"""


adiciona = """
Para adicionar um item na tabela, digite seu nome, preço e quantidade e precione executar: <br />

<!DOCTYPE html>
<html lang="en">
  <body>
    <section id="contact" class="section">
      <div class="container">
        <div class="row">
          <div class="col-lg-6 col-md-12">
          <form id="contactForm">
            <div class="row">
              <div class="col-md-12">
                <div class="form-group"> 
                  <textarea class="form-control" id="nome"  name="nome" placeholder="nome" rows="1" data-error="nome" required></textarea>
                  <div class="help-block with-errors"></div>
                </div>
              <div class="col-md-12">
                <div class="form-group"> 
                  <textarea class="form-control" id="preço"  name="preço" placeholder="preço" rows="1" data-error="preço" required></textarea>
                  <div class="help-block with-errors"></div>
                </div>
              <div class="col-md-12">
                <div class="form-group"> 
                  <textarea class="form-control" id="quantidade"  name="quantidade" placeholder="quantidade" rows="1" data-error="quantidade" required></textarea>
                  <div class="help-block with-errors"></div>
                </div>
                <div class="submit-button">
                  <button class="btn btn-common" id="submit" type="submit">Executar</button>
                  <div id="msgSubmit" class="h3 hidden"></div> 
                  <div class="clearfix"></div> 
                </div>
              </div>
            </div>            
          </form>
          </div>
        </div>
      </div>
    </section>
  </body>
</html>
"""

remove = """
<br />
Para remover um item da tabela, digite seu ID e precione executar: <br />

<!DOCTYPE html>
<html lang="en">
  <body>
    <section id="contact" class="section">
      <div class="container">
        <div class="row">
          <div class="col-lg-6 col-md-12">
          <form id="contactForm">
            <div class="row">
              <div class="col-md-12">
                <div class="form-group"> 
                  <textarea class="form-control" id="id"  name="id" placeholder="id" rows="1" data-error="id" required></textarea>
                  <div class="help-block with-errors"></div>
                </div>
                <div class="submit-button">
                  <button class="btn btn-common" id="submit" type="submit">Executar</button>
                  <div id="msgSubmit" class="h3 hidden"></div> 
                  <div class="clearfix"></div> 
                </div>
              </div>
            </div>            
          </form>
          </div>
        </div>
      </div>
    </section>
  </body>
</html>
"""

atualiza = """
<br /> <br />
Para atualizar a quantidade de um item na tabela, digite seu ID e nova quantidade, e precione executar: <br />

<!DOCTYPE html>
<html lang="en">
  <body>
    <section id="contact" class="section">
      <div class="container">
        <div class="row">
          <div class="col-lg-6 col-md-12">
          <form id="contactForm">
            <div class="row">
              <div class="col-md-12">
                <div class="form-group"> 
                  <textarea class="form-control" id="id"  name="id" placeholder="id" rows="1" data-error="id" required></textarea>
                  <div class="help-block with-errors"></div>
                </div>
                <div class="form-group"> 
                  <textarea class="form-control" id="quantidade"  name="quantidade" placeholder="quantidade" rows="1" data-error="quantidade" required></textarea>
                  <div class="help-block with-errors"></div>
                </div>
                <div class="submit-button">
                  <button class="btn btn-common" id="submit" type="submit">Executar</button>
                  <div id="msgSubmit" class="h3 hidden"></div> 
                  <div class="clearfix"></div> 
                </div>
              </div>
            </div>            
          </form>
          </div>
        </div>
      </div>
    </section>
  </body>
</html>
"""
