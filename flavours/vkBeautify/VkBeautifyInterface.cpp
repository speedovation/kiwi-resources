#include <QPlainTextEdit>
#include <QDebug>
#include <QInputDialog>
#include <QLineEdit>

#include "Interface.h"
#include "VkBeautifyInterface.h"

using Flavours::VkBeautifyInterface;


VkBeautifyInterface::VkBeautifyInterface(QPlainTextEdit *editor): Interface() , editor(editor)
{
    loadScriptFile(":/js/vkbeautify.js");
    loadScriptFile(":/js/interface.js");
}

void VkBeautifyInterface::beautify(QString mode)
{
    beautifyMinify(mode);
}

void VkBeautifyInterface::minify(QString mode)
{
    beautifyMinify(mode,true);
}

void VkBeautifyInterface::beautifyMinify(QString mode,bool isMinify)
{

    QString functionName = "beautify";

    if(isMinify)
        functionName = "minify";

    QTextCursor tc = editor->textCursor();

    if(!tc.hasSelection())
    {
        tc.select(QTextCursor::Document);
    }

    QString text = tc.selectedText();

    //(js_source_text, options)

    QString content = callJavascriptFunction(functionName,QStringList() << mode << text );

    if(content.isNull() || content.isEmpty() )
        return;

    tc.removeSelectedText();

    tc.insertText(text);

    editor->setTextCursor(tc);

}



