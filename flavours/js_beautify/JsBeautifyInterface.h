#include <QPlainTextEdit>
#include <QDebug>
#include "Interface.h"

//using Flavours;

namespace Flavours
{
    class JsBeautifyInterface : public Interface
    {

            Q_OBJECT

        public:
            JsBeautifyInterface();

            void test ();

        public slots:

            void beautifyHtml();
            void beautifyCss();
            void beautifyJs();
            void beautify(QString functionName);

        signals:

    };

} //end of Flavours namespace
