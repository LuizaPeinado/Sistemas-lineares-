<h1 alight = center> Programa criado para solucionar sistemas lineares sem limite de incógtas. </h1>

<h2> Para esse trabalho usamos a biblioteca NUMPY com o objetivo de usar suas funcionalidades com manipulação de matrizes e propriedades matématicas como Cramer e Gauss. </h2>

<h3> Primeiramente declaramos as coeficientes das equações dentro das Arrays. Logo em seguida, Contamos a quantidade de incogtas dentro da matriz A e comparamos com a quantidade de resultados dentro da Matriz B, assim, se os valores forem iguais, a matriz será quadrada. O contrário disso significa que a matriz não é quadrada,logo, não funcionará no código. Depois de verificar a condição de a Matriz ser quadrada, verificamos o valor do determinante, e se for igual a 0, a matriz será impossível e indeterminada. O contrário significa que a matriz é possível e determinada. Usando as funções da biblioteca NUMPY, encontramos a inversa da Matriz A (a matriz que contém os coeficientes) e aplicamos a propriedade de matrizes em que o inverso da Matriz A multiplicado pela matriz B (a matriz que contém os resultados) é igual a matriz que contém as incogtas. Assim, geramos a matriz contendo as incógtas. </h3>

<h3> Caso a Matriz seja impossível ou possível e indeterminada, o programa emitirá uma mensagem comunicando. </h3>
