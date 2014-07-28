#include <QPlainTextEdit>
#include <QDebug>
#include "Interface.h"

//using Flavours;

namespace Flavours
{
    class VkBeautifyInterface : public Interface
    {

            public:
                VkBeautifyInterface(QPlainTextEdit *editor);

                //Beautify Function
                //Mode 'XML' 'JSON' 'CSS'  'SQL'
                void beautify(QString mode);

                //Beautify Function
                void minify(QString mode);

                void beautifyMinify(QString mode,bool isMinify=false);


            private:
                QPlainTextEdit *editor;
        };

} //end of Flavours namespace
