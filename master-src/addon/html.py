def get_html(data_casper, data_balthasar, data_melchior):
  return '''
    <div class="body1">
        <div class="left-col">
            <div class="t1">
                <div class="t-border"></div>
                <div class="t-border"></div>
                <h2>提訴</h2>
                <div class="t-border"></div>
                <div class="t-border"></div>
            </div>
            <div class="code">
                <h3>CODE : 132</h3>
                <p>FILE:MAGI_SYS</p>
                <p>EXTENTION:2048</p>
                <p>EX_MODE:ON</p>
                <p>PRIORITY:A__</p>
            </div>
        </div>
        <div class="right-col">
            <div class="t2">
                <div class="t-border"></div>
                <div class="t-border"></div>
                <h2>決議</h2>
                <div class="t-border"></div>
                <div class="t-border"></div>
            </div>
            <div class="status">
                <h3 id="status">審議中</h3>
            </div>
        </div>
        <div class="circle">
            <div class="magi">MAGI</div>
        </div>
        <div class="box melchior">
            <div class="square">
                <h3>MELCHIOR</h3>
                <h2>1</h2>
            </div>
        </div>
        <div class="box balthasar">
            <div class="square">
                <h2>2</h2>
                <h3>BALTHASAR</h3>
            </div>
        </div>
        <div class="box casper">
            <div class="square">
                <h3>CASPER</h3>
                <h2>3</h2>
            </div>
        </div>
        <input type="button" id="button6" disabled style="display: none;" data-casper="%s" data-balthasar="%s" data-melchior="%s" />
        <script>
            function computing() {
                for (const element of document.getElementsByClassName(
                        'square')) {
                    if (element.classList.contains('square-flash')) {
                        element.classList.remove('square-flash');
                    }
                }
                let resultText = '否決';
                if (parseFloat(document.getElementById(
                    'button6').getAttribute(
                        'data-casper')) > 50) {
                    resultText = '承認';
                } else {
                    document.getElementsByClassName(
                        'casper')[0].firstChild.style.backgroundColor = '#fe6c6c';
                }
                if (parseFloat(document.getElementById(
                    'button6').getAttribute(
                        'data-balthasar')) < 50) {
                    document.getElementsByClassName(
                        'balthasar')[0].firstChild.style.backgroundColor = '#fe6c6c';
                }
                if (parseFloat(document.getElementById(
                    'button6').getAttribute(
                        'data-melchior')) < 50) {
                    document.getElementsByClassName(
                        'melchior')[0].firstChild.style.backgroundColor = '#fe6c6c';
                }
                document.getElementById('status').innerHTML = resultText;
            }
            computing();
        </script>
    </div>
  ''' %(data_casper, data_balthasar, data_melchior)
